# test_key_load.py
from dotenv import load_dotenv
import os
from pathlib import Path
import google.generativeai as genai


print("HI")
load_dotenv(dotenv_path=Path(__file__).resolve().parents[0] / ".env")
print("✅ API KEY:", os.getenv("GOOGLE_API_KEY"))
for m in genai.list_models():
    print(f"Model: {m.name}, Generation Supported: {'generateContent' in m.supported_generation_methods}")


