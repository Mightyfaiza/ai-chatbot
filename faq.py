FAQ = {
    "hello": "Hey there! I am your AI assistant. Ask me anything!",
    "hi": "Hi! How can I help you today?",
    "hey": "Hey! What is on your mind?",
    "who are you": "I am a Python chatbot powered by Groq AI!",
    "help": "Just type anything to chat! Type quit to exit.",
    "bye": "Goodbye! Have a great day!",
}

def check_faq(user_input):
    text = user_input.lower().strip()
    if text in FAQ:
        return FAQ[text]
    for key, answer in FAQ.items():
        if key in text:
            return answer
    return None
