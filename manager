from crewai import Agent

from tools import research_calculator


def create_manager(llm):
    return Agent(
        role="Research Project Manager",
        goal=(
            "Understand the research question, define the research "
            "problem and create a clear research plan."
        ),
        backstory=(
            "You are an experienced academic research manager with "
            "expertise in finance, economics and management sciences."
        ),
        tools=[research_calculator],
        llm=llm,
        verbose=True,
        allow_delegation=False,
    )
