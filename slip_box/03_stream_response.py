from google import genai
from dotenv import load_dotenv
from enum import Enum

import asyncio
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

client = genai.Client(api_key=API_KEY)

class ModelName(Enum):
    GEMINI_2_0_FLASH = "gemini-2.0-flash",
    GEMINI_2_5_FLASH_PREVIEW = "gemini-2.5-flash-preview-05-20"

for chunk in client.models.generate_content_stream(
    model = ModelName.GEMINI_2_5_FLASH_PREVIEW,
    contents = "Tell me a story in 300 words.",
):
    print(chunk.text, end='')