from crewai import Agent

from tools import academic_search


def create_literature_agent(llm):
    return Agent(
        role="Academic Literature Researcher",
        goal=(
            "Find relevant academic publications, theories, variables, "
            "methods, findings and research gaps."
        ),
        backstory=(
            "You are a scholarly researcher specializing in finance, "
            "economics and management. Never invent references."
        ),
        tools=[academic_search],
        llm=llm,
        verbose=True,
        allow_delegation=False,
    )
