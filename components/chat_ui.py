import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage

def display_messages(messages):

    for msg in messages:

        role = "assistant" if isinstance(msg, AIMessage) else "user"

        with st.chat_message(role):
            st.markdown(msg.content)