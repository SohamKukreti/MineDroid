import streamlit as st
import os
from googletrans import Translator
import chatbotCore  # Import the modified chatbotCore module

st.set_page_config(page_title="Multi-Page Landing", layout="wide")

menu = st.sidebar.selectbox("Navigation", ["Home", "ChatBot", "PDF_Reader", "Contact"])

def home_page():
    st.title("🧠 MineDroid")
    st.header("Welcome to the Home Page!")
    st.header("Select your Option from the Sidebar selectbox! 😃")
    st.header("We have 3 features available!")
    st.header("1) Chat Bot")
    st.header("2) PDF Reader")
    st.header("3) You can use the application on the Mobile Remote device")
    
def chatbot_page():
    st.title("🤖 ChatBot Page")
    st.write("This is the Chat_Bot Page. Here, you can ask your queries in any language.")
    
    # Create a text input field for user queries
    user_input = st.text_input("Enter your query:")
    
    if st.button("Ask"):
        if user_input:
            response = chatbotCore.run_chatbot(user_input)  # Call the chatbot function
            st.write("Bot's Response:")
            st.write(response)
        else:
            st.warning("Please enter a query before clicking 'Ask'.")

def pdf_reader():
    st.title("📖 PDF Reader!")
    st.write("This is the PDF reader!")
    st.write("Here, you can upload any PDF of yours and ask questions regarding it!")

def contact_page():
    st.title("Contact Page")
    st.write("Contact us at contact@example.com")

if menu == "Home":
    home_page()
elif menu == "ChatBot":
    chatbot_page()
elif menu == "PDF_Reader":
    pdf_reader()
elif menu == "Contact":
    contact_page()
