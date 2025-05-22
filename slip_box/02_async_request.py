from google import genai
from dotenv import load_dotenv
import asyncio

import os

load_dotenv()

API_KEY = os.getenv("API_KEY")


client = genai.Client(api_key=API_KEY)
model = "gemini-2.0-flash",
model = "gemini-2.5-flash-preview-05-20"


async def main():

    response = await client.aio.models.generate_content(
        model=model,
        contents="make summary of this video: https://youtu.be/bwz3Z9GXLyI?si=-pr157wnyggKjwxL"
    )

    print(response.text)

asyncio.run(main())