from pathlib import Path
from typing import List

from pydantic import BaseModel, Field
from transformers import pipeline

# ----------- Mental Health Support Agent -------------
class MentalHealthSupportAgent:
    def _init_(self):
        self.model = pipeline(
            "text-generation",
            model="meta-llama/Llama-3.2-1B-Instruct",
            max_new_tokens=150,
        )

    def respond(self, user_message: str) -> str:
        prompt = (
            "You are a kind, supportive mental health assistant. "
            "Give warm, gentle, encouraging replies. Keep them short.\n"
            f"User: {user_message}\nAssistant:"
        )
        output = self.model(prompt)[0]["generated_text"]
        return output.split("Assistant:")[-1].strip()


# ----------- Main function -------------
def run_mh_agent(user_message: str) -> str:
    agent = MentalHealthSupportAgent()
    return agent.respond(user_message)


# Example test (will not run on Spaces UI)
if _name_ == "_main_":
    print(run_mh_agent("I feel stressed today."))
