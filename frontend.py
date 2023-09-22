# launch with streamlit run frontend.py in terminal

import ml_chat
import streamlit as st
from streamlit import chat_message 

st.title("App To Chat With DataBase")
st.write("You can ask me all the questions and let the Support Team rest!!")

if 'questions' not in st.session_state:
    st.session_state.questions = []
if 'answers' not in st.session_state:
    st.session_state.answers = []

def click():
    if st.session_state.user != '':
        question = st.session_state.user
        answer = ml_chat.question(question)

        st.session_state.questions.append(question)
        st.session_state.answers.append(answer)

        # Clear user input after submitting question
        st.session_state.user = ''


with st.form('my-form'):
   question = st.text_input('¿How I can help you?:', key='user', help='Press Send to make the question')
   submit_button = st.form_submit_button('Send',on_click=click)

if st.session_state.questions:
    for i in range(len(st.session_state.answers)-1, -1, -1):
        chat_message(st.session_state.answers[i], key=str(i))

    # Option to continue the conversation
    continue_conversation = st.checkbox('Do you want to make another question?')
    if not continue_conversation:
        st.session_state.questions = []
        st.session_state.answers = []









