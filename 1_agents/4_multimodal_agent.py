import os
import json
from agno.agent import Agent
from agno.models.google import Gemini
from agno.media import Image
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model=Gemini(id="gemini-2.0-flash"),    
    tools=[],
)

response = agent.run(
    message='''     
    for each image, generate a json record looks like this:
    {
        "item_name": "sari",
        "item_code": "ITM-0001",
        "item_color": "red",
        "gender": "female",
        "age_category": "adult"
    }
    item_name should be like sari, jacket, shirt, pant etc.
    item_code should be like ITM-0001, ITM-0002 etc and unique for each item.
    age_category should be one of the following: adult, child
    output should be in json string for a list of JSON object. No preamble or postamble text, just the JSON string.
    ''',
    images=[
        Image(filepath=os.path.join(Path(__file__).parent, "images", "image_1.jpg")),
    ]
)

response_raw = response.content
# Remove markdown fences
if response_raw.startswith("```"):
    response_raw = response_raw.replace("```", "").replace("json", "").strip()


# convert to JSON
if response_raw:
    try:
        response_json = json.loads(response_raw)
        print(response_json)
    except json.JSONDecodeError as e:
        print("Failed to parse JSON:", e)
        print("Raw response:", response.content)
else:
    print("Empty response received!")
    print("Status code:", response.status_code)