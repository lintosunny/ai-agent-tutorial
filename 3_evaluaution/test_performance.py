from agno.agent import Agent
from agno.eval.performance import PerformanceEval
from agno.models.google import Gemini

from inventory_agent import inventory_agent

def agent_call():
    response = inventory_agent.run("What is the stock status of iPhone 15?")
    return response

simple_response_perf = PerformanceEval(
    func=agent_call, num_iterations=3, warmup_runs=0
)

if __name__ == "__main__":
    simple_response_perf.run(print_results=True, print_summary=True)