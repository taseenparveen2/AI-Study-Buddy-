from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

def get_llm(model_name="llama-3.1-8b-instant"):
    return Groq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name=model_name
    )