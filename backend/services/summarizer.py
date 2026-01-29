import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def summarize_text(text: str):
    return {
        "summary": "Voice note successfully transcribed."
        
    }

