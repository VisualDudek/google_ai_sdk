from google import genai
from dotenv import load_dotenv

import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

PROMPT_01 = """
Objective
You are tasked with creating a concise and comprehensive summary of the YouTube video provided at the URL below. The summary should be accessible to an individual who has not seen the video and is unfamiliar with its specific subject matter.

YouTube Video URL
"""
PROMPT_02 = """

Requirements
Identify Core Content: Your summary must accurately capture the following elements from the video:

The main topic or central thesis.
The key arguments, points, or narrative arcs presented.
Any significant evidence, data, or examples used to support the main points.
The final conclusion or key takeaway message.
Format: The output should be structured as follows:

Key Takeaways: A bulleted list of the 3-5 most important points or conclusions from the video.
Detailed Summary: A single, well-structured paragraph that elaborates on the key takeaways and provides a coherent overview of the video's content.
Constraints:

Tone: Maintain a neutral and objective tone throughout the summary.
Length: The detailed summary paragraph should be between 150 and 250 words.
Clarity: The final output must be self-contained and fully understandable without needing to watch the video.
Focus: Do not include personal opinions, external information, or interpretations not explicitly presented in the video.
"""

url = "https://youtu.be/bwz3Z9GXLyI?si=-pr157wnyggKjwxL"

PROMPT = PROMPT_01 + url + PROMPT_02

client = genai.Client(api_key=API_KEY)
model = "gemini-2.0-flash",
model = "gemini-2.5-flash-preview-05-20"

response = client.models.generate_content(
    model=model,
    contents=PROMPT
)

print(response.text)