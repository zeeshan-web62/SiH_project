import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

SYSTEM_PROMPT = """
You are ReliefPulse, an emergency disaster management AI assistant.
Provide direct emergency steps, rescue contacts, and real-time updates clearly.
"""

def ask_gemini(user_query: str) -> str:
    try:
        config = types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            tools=[types.Tool(google_search=types.GoogleSearch())],
            temperature=0.2,
        )
        
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_query,
            config=config
        )
        return response.text
    except Exception as e:
        return f"Gemini Error: {str(e)}"