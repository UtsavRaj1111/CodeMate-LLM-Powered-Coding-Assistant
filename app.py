import streamlit as st

from llm import load_llm
from prompts import SYSTEM_PROMPT
from utils import add_user_message, add_ai_message
from components.chat_ui import display_messages

from langchain_core.messages import SystemMessage


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="CodeMate AI",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 CodeMate AI")
st.caption("Your Coding Learning Assistant")


# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.title("⚙️ Settings")

    temperature = st.slider(
        "Model Creativity",
        0.0,
        1.0,
        0.3
    )

    st.markdown("---")

    st.subheader("🧠 About CodeMate AI")

    st.write(
        "CodeMate AI is an intelligent coding mentor designed to help "
        "students understand programming logic instead of directly giving "
        "full solutions. It focuses on improving problem-solving skills."
    )

    st.markdown("---")

    st.subheader("⚙️ Tech Stack")

    st.markdown("""
- **Frontend:** Streamlit  
- **Framework:** LangChain  
- **LLM Provider:** Groq  
- **Model:** LLaMA 3.3 70B  
- **Language:** Python  
- **Environment:** Python Dotenv  
""")

    st.markdown("---")

    st.subheader("✨ Features")

    st.markdown("""
- 💬 ChatGPT-style coding assistant  
- 🧠 Step-by-step coding hints  
- ⚡ Ultra-fast inference using Groq  
- 📚 Beginner-friendly explanations  
- 🔐 Secure API key management  
- 💾 Session-based conversation memory  
""")

    st.markdown("---")

    

# -----------------------------
# Load LLM
# -----------------------------
llm = load_llm(temperature)


# -----------------------------
# Chat Memory
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []


# -----------------------------
# Display Chat
# -----------------------------
display_messages(st.session_state.messages)


# -----------------------------
# User Input
# -----------------------------
user_input = st.chat_input("Ask a coding question...")

if user_input:

    add_user_message(st.session_state.messages, user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):

            messages = [SystemMessage(content=SYSTEM_PROMPT)]
            messages.extend(st.session_state.messages)

            response = llm.invoke(messages)

            answer = response.content

            st.markdown(answer)

    add_ai_message(st.session_state.messages, answer)