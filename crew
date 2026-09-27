import os

from crewai import Crew, LLM, Process, Task

from manager import create_manager
from literature_agent import create_literature_agent
from methodology_agent import create_methodology_agent
from reviewer_agent import create_reviewer_agent
from writer_agent import create_writer_agent


MODEL = "groq/openai/gpt-oss-120b"


def create_llm():
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError(
            "GROQ_API_KEY is missing. Add it in Streamlit Secrets."
        )

    return LLM(
        model=MODEL,
        api_key=api_key,
        temperature=0.2,
        reasoning_effort="medium",
    )


def run_research(question: str):
    llm = create_llm()

    manager = create_manager(llm)
    literature = create_literature_agent(llm)
    methodology = create_methodology_agent(llm)
    reviewer = create_reviewer_agent(llm)
    writer = create_writer_agent(llm)

    manager_task = Task(
        description=f"""
        Analyze this research question:

        {question}

        Produce:
        1. Research problem
        2. Main objective
        3. Specific objectives
        4. Key concepts
        5. Important research areas
        6. Possible research gap

        Do not invent evidence.
        """,
        expected_output="A structured research plan.",
        agent=manager,
    )

    literature_task = Task(
        description=f"""
        Investigate the academic literature for:

        {question}

        You MUST use the Academic Literature Search tool.

        Identify:
        - relevant studies
        - theories
        - variables
        - methodologies
        - findings
        - disagreements
        - research gaps

        Never invent references.
        """,
        expected_output=(
            "A structured literature review with source information, "
            "major themes and research gaps."
        ),
        agent=literature,
        context=[manager_task],
    )

    methodology_task = Task(
        description=f"""
        Develop a PROPOSED empirical methodology for:

        {question}

        Based on the previous research, identify:
        - research design
        - dependent variable
        - independent variables
        - moderators/mediators where appropriate
        - control variables
        - measurements
        - hypotheses
        - model specification
        - estimation technique
        - robustness tests

        Use the Research Calculator when numerical calculations are needed.

        Do not present proposed methods as actual results.
        """,
        expected_output="A rigorous proposed research methodology.",
        agent=methodology,
        context=[manager_task, literature_task],
    )

    review_task = Task(
        description=f"""
        Critically review the research work for:

        {question}

        Check:
        - evidence quality
        - research gap
        - theoretical consistency
        - variables
        - hypotheses
        - methodology
        - model specification
        - unsupported claims
        - references

        Use Academic Literature Search or Research Source Checker
        when source verification is needed.

        Give specific corrections.
        """,
        expected_output=(
            "A critical academic review with weaknesses and "
            "specific recommended corrections."
        ),
        agent=reviewer,
        context=[manager_task, literature_task, methodology_task],
    )

    writing_task = Task(
        description=f"""
        Write a professional academic research report based ONLY
        on the team's research work.

        Research question:
        {question}

        Include:
        1. Proposed Title
        2. Background
        3. Research Problem
        4. Research Objectives
        5. Literature Review
        6. Research Gap
        7. Theoretical Foundation
        8. Conceptual Framework
        9. Hypotheses
        10. Methodology
        11. Variables and Measurements
        12. Proposed Model
        13. Limitations
        14. Future Research
        15. Verified Sources

        IMPORTANT:
        Never fabricate authors, papers, DOI numbers, journals,
        statistics, regression results, p-values or empirical findings.

        Clearly label proposed methodology as proposed.
        """,
        expected_output="A professional academic research report.",
        agent=writer,
        context=[
            manager_task,
            literature_task,
            methodology_task,
            review_task,
        ],
    )

    crew = Crew(
        agents=[
            manager,
            literature,
            methodology,
            reviewer,
            writer,
        ],
        tasks=[
            manager_task,
            literature_task,
            methodology_task,
            review_task,
            writing_task,
        ],
        process=Process.sequential,
        verbose=True,
    )

    return crew.kickoff()
