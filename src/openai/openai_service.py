import openai
from src.openai.openai_config import *
openai.api_key = api_key

# Product knowledge
product_info = {
    'product_name': 'Your Product',
    'description': 'A brief description of your product.',
    'features': ['Feature 1', 'Feature 2', 'Feature 3'],
    'pricing': 'Our product is competitively priced at $X. We also offer different plans to suit your needs.',
}

# Initial chat prompt

class Openai_Service:
    chat_history = []

    def chatbot(self,chat_history:list):
        print(f"Sales Bot: Hello! Welcome to {product_info['product_name']} support. How can I assist you today?")

        response = self.generate_response(chat_history=chat_history)
        chat_history.append(f"Sales Bot: {response}")
            
        print(f"Sales Bot: {response}")
        return {
            'response': response, 
            'chat_history':chat_history
        }

    def generate_response(self,chat_history):
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages = chat_history,
            temperature=1,
            max_tokens=64,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return response.choices[0].message.content

    if __name__ == "__main__":
        chatbot()
