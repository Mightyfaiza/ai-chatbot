import os
from dotenv import load_dotenv
from groq import Groq
from faq import check_faq

load_dotenv()
client = Groq()
conversation_history = []
SYSTEM_PROMPT = 'You are a friendly helpful AI assistant. Keep answers clear and concise.'

def ask_groq(user_message):
    conversation_history.append({'role': 'user', 'content': user_message})
    response = client.chat.completions.create(model='llama-3.1-8b-instant', messages=[{'role': 'system', 'content': SYSTEM_PROMPT}, *conversation_history], temperature=0.7, max_tokens=512)
    bot_reply = response.choices[0].message.content
    conversation_history.append({'role': 'assistant', 'content': bot_reply})
    return bot_reply

def chat(user_input):
    faq_answer = check_faq(user_input)
    if faq_answer:
        return faq_answer, 'FAQ'
    return ask_groq(user_input), 'Groq AI'

def main():
    print('AI Chatbot - Powered by Groq')
    print('Type quit to exit, clear to reset')
    while True:
        try:
            user_input = input('You: ').strip()
        except (KeyboardInterrupt, EOFError):
            break
        if not user_input:
            continue
        if user_input.lower() in ('quit', 'exit'):
            print('Bot: Goodbye!')
            break
        if user_input.lower() == 'clear':
            conversation_history.clear()
            print('Bot: Memory cleared!')
            continue
        try:
            response, source = chat(user_input)
            print(f'Bot [{source}]: {response}')
        except Exception as e:
            print(f'Bot: Error: {e}')

if __name__ == '__main__':
    main()
