# Level 3: Agents with memory and reasoning

from agno.agent import Agent 
from agno.models.google import Gemini
from agno.tools.reasoning import ReasoningTools
from agno.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model=Gemini(id="gemini-2.0-flash"),
    tools=[
        ReasoningTools(add_instructions=True),
        YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True),
    ],
    instructions=[
        "use tables to display data",
        "only output the report, no other text",
    ],
    markdown=True,
)

agent.print_response(
    message="Write a report on NVIDIA",
    stream=True,
    show_full_reasoning=True,
    stream_intermediate_steps=True,
    show_thoughts=True,
)