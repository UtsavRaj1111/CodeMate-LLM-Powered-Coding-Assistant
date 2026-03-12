from langchain_core.messages import HumanMessage, AIMessage

def add_user_message(messages, text):
    messages.append(HumanMessage(content=text))

def add_ai_message(messages, text):
    messages.append(AIMessage(content=text))