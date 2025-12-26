import streamlit as st
from llm_handler import LLMHandler
from utils import save_candidate_data, is_exit_command, analyze_sentiment
from prompts import SYSTEM_ROLE

st.set_page_config(page_title="TalentScout Assistant", page_icon="🤖")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": SYSTEM_ROLE}]
    greeting = "Hello! I am Scout, the Hiring Assistant for TalentScout. I'm here to screen you for your desired role. To get started, please provide your **Full Name**."
    st.session_state.messages.append({"role": "assistant", "content": greeting})

if "step" not in st.session_state:
    st.session_state.step = "gather_name"

if "candidate_info" not in st.session_state:
    st.session_state.candidate_info = {}

st.sidebar.title("TalentScout 🤖")
st.sidebar.markdown("Powered by **Groq Llama 3.3**")
api_key = st.sidebar.text_input("Enter Groq API Key", type="password")

if st.sidebar.button("Clear Conversation"):
    st.session_state.clear()
    st.rerun()

llm = LLMHandler(api_key if api_key else None)

def process_input(user_input):
    if is_exit_command(user_input):
        st.session_state.step = "end"
        return "Thank you for your time! We have recorded your information. Goodbye!"

    step = st.session_state.step
    response = ""

    if step == "gather_name":
        st.session_state.candidate_info['name'] = user_input
        st.session_state.step = "gather_contact"
        response = f"Nice to meet you, {user_input}. Please provide your **Email Address** and **Phone Number**."

    elif step == "gather_contact":
        st.session_state.candidate_info['contact'] = user_input
        st.session_state.step = "gather_position"
        response = "Thank you. What is your **Desired Position** and **Current Location**?"

    elif step == "gather_position":
        st.session_state.candidate_info['position_location'] = user_input
        st.session_state.step = "gather_exp"
        response = "Great. How many **Years of Experience** do you have in this field?"

    elif step == "gather_exp":
        st.session_state.candidate_info['experience'] = user_input
        st.session_state.step = "gather_stack"
        response = "Got it. Now, please list your **Tech Stack** (languages, frameworks, databases, tools)."

    elif step == "gather_stack":
        st.session_state.candidate_info['tech_stack'] = user_input
        st.session_state.step = "quiz"
        
        with st.spinner("Generating tailored technical questions..."):
            questions = llm.generate_tech_questions(user_input)
        
        st.session_state.questions = questions 
        response = f"Excellent. Based on your stack, here are a few technical questions:\n\n{questions}\n\n**Please provide your answers below.**"

    elif step == "quiz":
        # Sentiment Analysis
        label, score = analyze_sentiment(user_input)
        st.session_state.candidate_info['tech_answers'] = user_input
        st.session_state.candidate_info['sentiment'] = label
        
        st.sidebar.markdown("### 📊 Communication Analysis")
        st.sidebar.info(f"Tone: **{label}**") 

        st.session_state.step = "end"
        save_candidate_data(st.session_state.candidate_info)
        
        response = "Thank you for your answers! I've saved your profile and responses. Our recruitment team will review them and reach out shortly. Have a great day!"

    elif step == "end":
        response = "The interview has concluded. Please refresh to restart."

    return response

st.title("TalentScout Hiring Assistant")

for msg in st.session_state.messages:
    if msg['role'] != 'system':
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

if prompt := st.chat_input("Type your response here..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    if st.session_state.step == "end":
        bot_reply = "The interview is over. Please refresh to restart."
    else:
        bot_reply = process_input(prompt)
    
    with st.chat_message("assistant"):
        st.markdown(bot_reply)
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})