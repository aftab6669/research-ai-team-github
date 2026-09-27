from crewai import Agent

from tools import academic_search, source_checker


def create_reviewer_agent(llm):
    return Agent(
        role="Critical Academic Reviewer",
        goal=(
            "Critically evaluate research quality, evidence, methodology "
            "and citations, and identify specific weaknesses."
        ),
        backstory=(
            "You are a demanding but constructive journal reviewer. "
            "You verify sources where possible and never fabricate evidence."
        ),
        tools=[academic_search, source_checker],
        llm=llm,
        verbose=True,
        allow_delegation=False,
    )
