from dotenv import load_dotenv

load_dotenv()

from typing import Optional

from agno.agent import Agent
from agno.models.google import Gemini

# ------------------ Inventory Tool (Mock) ------------------
def inventory_tool(product_name):
    """
    Retrieve the stock status of a specified product.

    Args:
        product_name (str): The name of the product to check in the inventory.

    Returns:
        str: A message indicating the stock status and available quantity
             if the product exists, or "Product not found in inventory."
             if the product is not listed.
    """
    inventory = {
        "iPhone 15": "In Stock: Available Items = 2",
        "AirPods Pro": "Out of Stock: Available Items = 0",
        "MacBook Air M3": "In Stock: Available Items = 5"
    }
    return inventory.get(product_name, "Product not found in inventory.")
    

# ------------------ Inventory Agent ------------------
inventory_agent = Agent(
    name="Inventory Agent",
    model=Gemini(id="gemini-2.0-flash"),
    tools=[inventory_tool],
    instructions=["""
    You are an inventory assistant.

    - If a question is out of scope which is not related to inventory then just say ""Sorry, I can’t assist with that."
    - When a user asks about a product, extract the exact product name from their query and call the inventory_tool(product_name="...") with it.

    - Always call the inventory_tool with the full product name.
    - inventory_tool will return a dictionary which you need to parse to extract stock status, inventory items etc.
    - Respond with clear, concise information including:
        1. The stock status (e.g., "In Stock", "Out of Stock")
        2. The number of available items (if applicable)
    - If the product is not found, say: "The product is not available in our inventory."

    Never guess or hallucinate information. Do not respond unless the inventory_tool is called.
    Keep your response short and informative.
    """],
    show_tool_calls=True,
    markdown=True,
)

inventory_agent.print_response("I want to buy AirPods Pro, is it available?", stream=False)