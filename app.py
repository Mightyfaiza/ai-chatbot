import streamlit as st
from dotenv import load_dotenv
from groq import Groq
from faq import check_faq

load_dotenv()
client = Groq()
SYSTEM_PROMPT = 'You are a helpful AI assistant.'

def ask_groq(messages):
    r = client.chat.completions.create(model='llama-3.1-8b-instant', messages=[{'role':'system','content':SYSTEM_PROMPT},*messages], max_tokens=512)
    return r.choices[0].message.content

def chat(user_input, history):
    faq = check_faq(user_input)
    if faq: return faq, 'FAQ'
    return ask_groq(history), 'Groq AI'

st.title('AI Chatbot')
if 'messages' not in st.session_state: st.session_state.messages = []
if 'history' not in st.session_state: st.session_state.history = []
if st.button('Clear'): st.session_state.messages = []; st.session_state.history = []; st.rerun()
for msg in st.session_state.messages:
    with st.chat_message(msg['role']): st.write(msg['content'])
if u := st.chat_input('Type here...'):
    st.session_state.messages.append({'role':'user','content':u})
    st.session_state.history.append({'role':'user','content':u})
    with st.chat_message('user'): st.write(u)
    with st.chat_message('assistant'):
        try:
            res, src = chat(u, st.session_state.history)
            st.write(res); st.caption(src)
            st.session_state.messages.append({'role':'assistant','content':res})
            st.session_state.history.append({'role':'assistant','content':res})
        except Exception as e: st.error(str(e))