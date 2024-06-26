import streamlit as st
import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
prompt = [{"role":"system","content":"You are a chatbot that is always lying"}]

def generation(question) :
    answer = openai.ChatCompletion.create(model = "gpt-3.5-turbo", messages = question)
    return answer["choices"][0]["message"]["content"]

st.title("Open AI Generation")
question = st.text_input("Enter your question : ")
button = st.button("Generate")

if "history" not in st.session_state:
    st.session_state.history = prompt

for message in st.session_state.history:
    if message['role'] == 'user':
        st.write(f"**User**: {message['content']}")
    else:
        st.write(f"**Assistant**: {message['content']}")
if button:
    if question:
        st.session_state.history.append({"role":"user","content":question})
        answer = generation(st.session_state.history)
        st.session_state.history.append({"role":"assistant","content" : answer})
        st.write(st.session_state.history)
        
        st.experimental_rerun()
        st.session_state.question = ""

