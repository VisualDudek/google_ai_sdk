from google import genai
from dotenv import load_dotenv
from enum import Enum
from google.genai import types

import asyncio
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")


client = genai.Client(api_key=API_KEY)

class ModelName(Enum):
    GEMINI_2_0_FLASH = "gemini-2.0-flash",
    GEMINI_2_5_FLASH_PREVIEW = "gemini-2.5-flash-preview-05-20"


async def main():

    #         vvvvvvvvvvvvvvvvvvvvvvvvvvvv type hinting for response
    response: types.GenerateContentResponse = await client.aio.models.generate_content(
        model = ModelName.GEMINI_2_5_FLASH_PREVIEW,
        contents = "Why is the sky blue?",
    )

    print(response.text)
    print(response)


asyncio.run(main())