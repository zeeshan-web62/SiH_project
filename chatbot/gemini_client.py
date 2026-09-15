import os
try:
    from google import genai
except ImportError:
    genai = None
from dotenv import load_dotenv

# .env file se environment variables load karein
load_dotenv()

# Environment variable se key read karein
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def ask_gemini(prompt: str) -> str:
    if genai is None:
        return "Gemini is unavailable because the google-genai package is not installed."
    if not GEMINI_API_KEY:
        return "Gemini is unavailable because GEMINI_API_KEY is not configured."

    try:
        client = genai.Client(api_key=GEMINI_API_KEY)
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text or "Gemini returned an empty response."
    except Exception as e:
        return f"Gemini API Error: {str(e)}"