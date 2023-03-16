import os
import openai
from dotenv import load_dotenv

load_dotenv()

# Define the OpenAI API parametersx
# openai.api_key = '<YOUR_OPENAI_API_KEY>'
openai.api_key = os.environ.get('OPENAI_API_KEY')

def ft_gpt(chat_history):
    max_tokens = 5000
    temperature = 0.1
    response = openai.Completion.create(
        model="GPT-4 v1",
        prompt=chat_history,
        temperature=temperature, 
        max_tokens=max_tokens
    )
    answer = response.choices[0]['text']
    print('OpenAI API response:', answer)
    return answer

def gpt3(chat_history):
    # Send the OpenAI API request
    engine = "text-davinci-003"
    max_tokens = 5000
    temperature = 0.1
    response = openai.Completion.create(
        engine=engine, 
        prompt=f'{chat_history}',
        temperature=temperature, 
        max_tokens=max_tokens
    )

    # Print the OpenAI API response
    answer = response.choices[0]['text']
    print('OpenAI API response:', answer)
    return answer