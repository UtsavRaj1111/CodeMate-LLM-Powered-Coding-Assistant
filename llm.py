from langchain_openai import ChatOpenAI
from config import GROQ_API_KEY, MODEL_NAME

def load_llm(temperature):

    llm = ChatOpenAI(
        model=MODEL_NAME,
        temperature=temperature,
        openai_api_key=GROQ_API_KEY,
        openai_api_base="https://api.groq.com/openai/v1",
    )

    return llm