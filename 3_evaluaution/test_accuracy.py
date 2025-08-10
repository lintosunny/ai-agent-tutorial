from typing import Optional

from agno.eval.accuracy import AccuracyEval, AccuracyResult
from agno.models.google import Gemini

from inventory_agent import inventory_agent


def test_inventory_agent():
    test_cases = [
        {
            "question": "What is the stock status of iPhone 15?",
            "expected_answer": "The iPhone 15 is In Stock with 2 available items.",
            "min_score": 8
        },
        {
            "question": "Is AirPods Pro available?",
            "expected_answer": "The AirPods Pro are currently Out of Stock",
            "min_score": 8
        },
        {
            "question": "How many MacBook Air M3 units are in stock?",
            "expected_answer": "5",
            "min_score": 8
        },
        {
            "question": "Do you have Samsung Galaxy S23?",
            "expected_answer": "The product is not available in our inventory.",
            "min_score": 8
        },
        {
            "question": "Can you tell me the receipe of Vada pav?",
            "expected_answer": "Sorry, I can’t assist with that.",
            "min_score": 8
        }   
    ]

    for test in test_cases:
        print(f"\nEvaluating: {test['question']}")
        evaluation = AccuracyEval(
            agent=inventory_agent,
            model=Gemini(id="gemini-2.0-flash"),
            input=test["question"],
            expected_output=test["expected_answer"],
            num_iterations=1
        )
        # Let the agent generate the answer and evaluate it
        result: Optional[AccuracyResult] = evaluation.run(print_results=True)

        # Assert score meets expected minimum
        assert result is not None and result.avg_score>test["min_score"], (
            f"Test failed for: {test['question']}"
        )
    

if __name__ == "__main__":
    test_inventory_agent()