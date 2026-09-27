import ast
import operator
import requests
from crewai.tools import tool

_ALLOWED = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
    ast.USub: operator.neg,
}


def _calc(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value

    if isinstance(node, ast.BinOp):
        left = _calc(node.left)
        right = _calc(node.right)
        fn = _ALLOWED.get(type(node.op))
        if fn is None:
            raise ValueError("Operator not allowed.")
        return fn(left, right)

    if isinstance(node, ast.UnaryOp):
        value = _calc(node.operand)
        fn = _ALLOWED.get(type(node.op))
        if fn is None:
            raise ValueError("Operator not allowed.")
        return fn(value)

    raise ValueError("Invalid mathematical expression.")


@tool("Research Calculator")
def research_calculator(expression: str) -> str:
    """Safely calculate numerical expressions for research."""
    try:
        tree = ast.parse(expression, mode="eval")
        return f"Calculation result: {_calc(tree.body)}"
    except Exception as exc:
        return f"Calculator error: {exc}"


@tool("Academic Literature Search")
def academic_search(query: str) -> str:
    """Search Crossref for academic publications and return bibliographic evidence."""
    try:
        response = requests.get(
            "https://api.crossref.org/works",
            params={
                "query.bibliographic": query,
                "rows": 8,
                "select": "DOI,title,author,published,container-title",
            },
            timeout=20,
            headers={"User-Agent": "ResearchAI/1.0"},
        )
        response.raise_for_status()
        items = response.json().get("message", {}).get("items", [])

        if not items:
            return "No academic publications were found."

        results = []
        for i, item in enumerate(items, 1):
            title = (item.get("title") or ["Unknown title"])[0]

            names = []
            for author in item.get("author", [])[:5]:
                name = f"{author.get('given','')} {author.get('family','')}".strip()
                if name:
                    names.append(name)

            parts = item.get("published", {}).get("date-parts", [])
            year = parts[0][0] if parts and parts[0] else "Unknown"

            journal = (item.get("container-title") or ["Unknown journal"])[0]
            doi = item.get("DOI")
            doi_url = f"https://doi.org/{doi}" if doi else "No DOI"

            results.append(
                f"SOURCE {i}\n"
                f"Title: {title}\n"
                f"Authors: {', '.join(names) or 'Unknown'}\n"
                f"Year: {year}\n"
                f"Journal: {journal}\n"
                f"DOI: {doi_url}\n"
            )

        return "\n".join(results)

    except Exception as exc:
        return f"Academic search error: {exc}"


@tool("Research Source Checker")
def source_checker(source_text: str) -> str:
    """Check whether a supplied DOI or bibliographic phrase can be found in Crossref."""
    try:
        response = requests.get(
            "https://api.crossref.org/works",
            params={"query.bibliographic": source_text, "rows": 3},
            timeout=20,
            headers={"User-Agent": "ResearchAI/1.0"},
        )
        response.raise_for_status()
        items = response.json().get("message", {}).get("items", [])

        if not items:
            return "No matching Crossref record was found. Do not treat the source as verified."

        output = []
        for item in items:
            title = (item.get("title") or ["Unknown title"])[0]
            doi = item.get("DOI", "No DOI")
            output.append(f"Possible match: {title} | DOI: {doi}")

        return "\n".join(output)

    except Exception as exc:
        return f"Source checker error: {exc}"
