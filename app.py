import streamlit as st

from crew import run_research


st.set_page_config(
    page_title="ResearchAI",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    .stApp {
        background:
            radial-gradient(circle at 10% 10%, rgba(59,130,246,.12), transparent 30%),
            radial-gradient(circle at 90% 10%, rgba(124,58,237,.12), transparent 30%),
            #07111f;
    }

    .block-container {
        max-width: 1180px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }

    .hero {
        padding: 2.4rem;
        border-radius: 26px;
        background: linear-gradient(135deg, rgba(15,23,42,.98), rgba(30,41,59,.92));
        border: 1px solid rgba(148,163,184,.16);
        box-shadow: 0 20px 70px rgba(0,0,0,.25);
        margin-bottom: 1.5rem;
    }

    .eyebrow {
        color: #60a5fa;
        font-size: .8rem;
        font-weight: 800;
        letter-spacing: .14em;
        margin-bottom: .7rem;
    }

    .hero h1 {
        font-size: 3.1rem;
        letter-spacing: -.05em;
        margin: 0;
    }

    .hero p {
        color: #cbd5e1;
        font-size: 1.05rem;
        max-width: 800px;
        line-height: 1.7;
        margin-top: 1rem;
    }

    .agent-card {
        background: rgba(15,23,42,.70);
        border: 1px solid rgba(148,163,184,.14);
        border-radius: 18px;
        padding: 1rem;
        margin-bottom: .7rem;
    }

    .agent-name {
        font-weight: 700;
        color: #f8fafc;
    }

    .agent-role {
        color: #94a3b8;
        font-size: .8rem;
        margin-top: .2rem;
    }

    .feature-card {
        background: rgba(15,23,42,.55);
        border: 1px solid rgba(148,163,184,.13);
        border-radius: 20px;
        padding: 1.2rem;
        height: 100%;
    }

    .feature-title {
        font-weight: 800;
        margin-bottom: .4rem;
    }

    .feature-text {
        color: #94a3b8;
        font-size: .88rem;
        line-height: 1.5;
    }

    .stButton > button {
        border-radius: 14px;
        min-height: 3.1rem;
        font-weight: 750;
    }

    textarea {
        border-radius: 16px !important;
    }

    section[data-testid="stSidebar"] {
        background: #050b14;
    }

    #MainMenu, footer {
        visibility: hidden;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero">
        <div class="eyebrow">MULTI-AGENT ACADEMIC RESEARCH</div>
        <h1>🔬 ResearchAI</h1>
        <p>
            A collaborative research team powered by CrewAI and
            Groq GPT-OSS 120B. Research literature, design methodology,
            critique evidence and prepare an academic research report.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.markdown("## 🔬 ResearchAI")
    st.caption("Your AI academic research team")

    st.markdown("### Agent Team")

    agents = [
        ("🧭", "Research Manager", "Research planning"),
        ("📚", "Literature Researcher", "Academic evidence"),
        ("📊", "Methodology Analyst", "Research design"),
        ("🔎", "Critical Reviewer", "Quality control"),
        ("✍️", "Academic Writer", "Final report"),
    ]

    for icon, name, role in agents:
        st.markdown(
            f"""
            <div class="agent-card">
                <div>{icon} <span class="agent-name">{name}</span></div>
                <div class="agent-role">{role}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.divider()
    st.caption("LLM: Groq • GPT-OSS 120B")
    st.caption("Framework: CrewAI")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-title">📚 Literature</div>
            <div class="feature-text">
                Searches Crossref for real academic publication metadata.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-title">📊 Methodology</div>
            <div class="feature-text">
                Develops variables, hypotheses, models and methods.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-title">🔎 Review</div>
            <div class="feature-text">
                Checks evidence, methodology and citation problems.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("")

st.markdown("## What do you want to research?")

question = st.text_area(
    "Research question",
    placeholder=(
        "Example: What is the impact of digital financial inclusion "
        "on banking sector stability in developing economies?"
    ),
    height=150,
    label_visibility="collapsed",
)

run = st.button(
    "🚀 Start Research Team",
    type="primary",
    use_container_width=True,
)

if run:
    if not question.strip():
        st.warning("Please enter a research question.")
        st.stop()

    st.markdown("---")
    st.markdown("## ⚡ Research Team Working")

    try:
        with st.status(
            "🔬 CrewAI is running the research team...",
            expanded=True,
        ) as status:
            st.write("🧭 Research Manager → planning")
            st.write("📚 Literature Researcher → searching academic sources")
            st.write("📊 Methodology Analyst → developing methodology")
            st.write("🔎 Critical Reviewer → checking quality")
            st.write("✍️ Academic Writer → preparing report")

            result = run_research(question.strip())

            status.update(
                label="✅ Research completed",
                state="complete",
                expanded=False,
            )

        st.markdown("---")
        st.markdown("## 📄 Research Report")
        st.markdown(str(result))

        st.download_button(
            "⬇️ Download Report",
            data=str(result),
            file_name="research_report.md",
            mime="text/markdown",
            use_container_width=True,
        )

    except Exception as error:
        st.error("The research team could not complete the task.")
        st.exception(error)

st.markdown("---")
st.caption("ResearchAI • CrewAI • Groq GPT-OSS 120B")
