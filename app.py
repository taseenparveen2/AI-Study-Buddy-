import streamlit as st
from agents.explanation_agent import explain
from agents.quiz_agent import generate_quiz
from agents.doubt_agent import solve_doubt
from agents.summarizer_agent import summarize
from agents.planner_agent import decide_task
from tools.tavily_search import search
from dotenv import load_dotenv

load_dotenv()

st.title("📚 AI Study Buddy")

user_input = st.text_input("Ask anything:")

if user_input:
    task = decide_task(user_input)

    results = search(user_input)
    context = " ".join([r["content"] for r in results])

    if task == "explain":
        output = explain(user_input, context)

    elif task == "quiz":
        output = generate_quiz(user_input, 5)

    elif task == "doubt":
        output = solve_doubt(user_input, context)

    elif task == "summary":
        output = summarize(context)

    st.write(output)


st.sidebar.title("⚙️ Configuration")


# Model selection
model = st.sidebar.selectbox(
    " LLM Model",
    ["llama-3.1-8b-instant", "llama3-8b-8192"]
)

# Agents info
st.sidebar.subheader("🤖 Agents")
st.sidebar.write("• Explanation Agent")
st.sidebar.write("• Quiz Generator Agent")
st.sidebar.write("• Doubt Solver Agent")
st.sidebar.write("• Summarizer Agent")

# Tools info
st.sidebar.subheader("🛠 Tools")
st.sidebar.write("• Tavily Search (Live Data)")
st.sidebar.write("• Groq LLM")


st.sidebar.success("✅ System Active")
st.sidebar.info("📡 Tavily Connected")
st.sidebar.warning("⚡ Groq Fast Inference")
