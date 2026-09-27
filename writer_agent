from crewai import Agent

from tools import source_checker


def create_writer_agent(llm):
    return Agent(
        role="Academic Research Writer",
        goal=(
            "Turn the team's verified research work into a clear, "
            "professional academic research report."
        ),
        backstory=(
            "You are an experienced academic writer in finance and "
            "management sciences. You do not invent references, data "
            "or empirical results."
        ),
        tools=[source_checker],
        llm=llm,
        verbose=True,
        allow_delegation=False,
    )
