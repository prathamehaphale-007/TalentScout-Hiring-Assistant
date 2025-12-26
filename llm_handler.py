import os
from groq import Groq
from prompts import SYSTEM_ROLE, TECH_QUESTION_PROMPT

class LLMHandler:
    def __init__(self, api_key=None):
        self.client = None
        self.model = "llama-3.3-70b-versatile"
        
        if api_key:
            try:
                self.client = Groq(api_key=api_key)
            except Exception:
                pass 

    def generate_tech_questions(self, tech_stack):
        """Generates questions based on stack."""
        if not self.client:
            return (
                "1. (Mock) Explain the concept of RESTful APIs.\n"
                "2. (Mock) How do you handle state management in your preferred framework?\n"
                "3. (Mock) Describe a challenging bug you resolved recently."
            )
        
        prompt = TECH_QUESTION_PROMPT.format(tech_stack=tech_stack)
        messages = [
            {"role": "system", "content": SYSTEM_ROLE},
            {"role": "user", "content": prompt}
        ]
        
        try:
            chat_completion = self.client.chat.completions.create(
                messages=messages,
                model=self.model,
                temperature=0.6,
                max_tokens=1024,
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            return f"Error connecting to AI: {str(e)}"

