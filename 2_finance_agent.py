# Level 2: Agents with knowledge and storage

from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()

def get_stock_symbol(company_name):
    """Extracts the stock symbol for a given company name.
    
    Args:
        company_name (str): The name of the company to find the stock symbol for.
        
    Returns:
        str: The stock symbol of the company.
    """
    symbols = {
        "abc_corp": "AAPL",        
        "Microsoft": "MSFT",
        "Google": "GOOGL",
        "Amazon": "AMZN",
    }
    return symbols.get(company_name, company_name)

agent = Agent(
    name="financial_agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True), get_stock_symbol],
    instructions=[ 
        "You are a financial analyst. Provide detailed stock analysis and recommendations.",
        "Always include the date of the analysis in your response.",
        "use tables to display stock data clearly.",
        "use get_stock_symbol if you cannot directly find the stock symbol using YFinanceTools.",
        "give me the analyis in as concise a manner as possible."
    ],
    show_tool_calls=True,
    markdown=True
)

agent.print_response(
    "What is the current stock price and analyst recommendations for Amazon?"
)