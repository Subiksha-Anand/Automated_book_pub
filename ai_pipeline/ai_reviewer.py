import os
from pathlib import Path
from dotenv import load_dotenv
import google.generativeai as genai




# 🌍 Load .env from project root directory
env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(dotenv_path=env_path)

# 🔑 Load the API key
api_key = os.getenv("GOOGLE_API_KEY")
print("🔑 Loaded GOOGLE_API_KEY:", api_key[:5] + "..." if api_key else "❌ NOT FOUND")

# ⚙️ Configure Gemini
genai.configure(api_key=api_key)

# 🚀 Load the Gemini model
model = genai.GenerativeModel('models/gemini-1.5-pro')

def review_chapter(text):
    prompt = (
        "You are a professional editor. Please review the following rewritten chapter. "
        "Correct grammar, improve clarity, and maintain the original tone and meaning.\n\n"
        f"{text}"
    )
    response = model.generate_content(prompt)
    return response.text
