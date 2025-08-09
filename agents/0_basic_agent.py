# Level 0: Agent with no tools (basic inference tasks)

from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    name="basic_agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    description="You are a news reporter. Using simple language to summarize the news into 3 lines along with date",
    markdown=True
)

agent.print_response(
    "What is the latest news about the war in Ukraine?"
)