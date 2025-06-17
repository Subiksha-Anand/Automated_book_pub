import os
from pathlib import Path
from dotenv import load_dotenv
import google.generativeai as genai



# 🌍 Load .env from project root directory (2 levels up from this file)
env_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(dotenv_path=env_path)

# 🔑 Get API key
api_key = os.getenv("GOOGLE_API_KEY")
print("🛠️ Loaded GOOGLE_API_KEY:", api_key[:5] + "..." if api_key else "❌ NOT FOUND")

# ⚙️ Configure Gemini
genai.configure(api_key=api_key)

# 🚀 Load model
model = genai.GenerativeModel('models/gemini-1.5-pro')
import time
from google.api_core.exceptions import ResourceExhausted

def spin_chapter(content):
    
    short_content = content[:2000]
    prompt = (
        "Rewrite the following chapter to make it more engaging and modern. "
        "Preserve the original meaning and style.\n\n"
        f"{content}"
    )
    
    for attempt in range(3):  # Retry up to 3 times
        try:
            response = model.generate_content(prompt)
            return response.text
        except ResourceExhausted:
            wait_time = 60  # Wait 60 seconds before retry
            print(f"⚠️ Rate limit hit. Waiting {wait_time} seconds before retrying...")
            time.sleep(wait_time)
    
    raise Exception("❌ Exceeded retry limit due to API rate limits.")
