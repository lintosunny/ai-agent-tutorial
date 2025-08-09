# Level 1: Agent with tools for autonomous task execution

from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.tools.duckduckgo import DuckDuckGoTools
load_dotenv()

agent = Agent(
    name="basic_agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGoTools()],
    description="You are a news reporter. Using simple language to summarize the news into 3 lines along with date",
    markdown=True
)

agent.print_response(
    "What is the latest news about the war in Ukraine?"
)