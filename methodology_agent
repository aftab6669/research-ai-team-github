from crewai import Agent

from tools import research_calculator


def create_methodology_agent(llm):
    return Agent(
        role="Research Methodology Analyst",
        goal=(
            "Develop a rigorous proposed research methodology, including "
            "variables, hypotheses, measurements and empirical models."
        ),
        backstory=(
            "You are an experienced quantitative researcher specializing "
            "in finance, econometrics and management sciences."
        ),
        tools=[research_calculator],
        llm=llm,
        verbose=True,
        allow_delegation=False,
    )
