import streamlit as st
import os
import random
from googletrans import Translator
import chatbotCore  # Import the modified chatbotCore module

st.set_page_config(page_title="Multi-Page Landing", layout="wide")

# Add your logo image file path here
logo_path = "logo.png"

menu = st.sidebar.selectbox("Navigation", ["Home", "ChatBot", "PDF_Reader", "Contact"])

facts = ["fact1","fact2","fact3","fact4","fact5","fact6","fact7","fact8","fact9","fact10","fact11"]

# Function to display the logo
def display_logo():
    st.sidebar.image(logo_path)

# Function to navigate to the ChatBot page
def navigate_to_chatbot():
    st.session_state.menu = "ChatBot"

# Function to navigate to the PDF Reader page
def navigate_to_pdf_reader():
    st.session_state.menu = "PDF_Reader"

# Function to navigate to the Mobile Device feature page
def navigate_to_mobile_device():
    st.session_state.menu = "Mobile_Device"

def home_page():
    display_logo()
    st.title("🤖 MineDroid")
    st.header("Welcome to the Home Page!")
    st.write("### Select your Option from the Sidebar selectbox! 😃")
    st.write("#### We have 3 features available!")
    
    # Create buttons to navigate to different pages
    if st.button("1) Chat Bot"):
        navigate_to_chatbot()
    if st.button("2) PDF Reader"):
        navigate_to_pdf_reader()
    if st.button("3) Mobile Device"):
        navigate_to_mobile_device()

def chatbot_page():
    display_logo()
    st.title("🧠 ChatBot Page")
    st.write("This is the Chat_Bot Page. Here, you can ask your queries in any language.")
    
    # Create a text input field for user queries
    user_input = st.text_input("Enter your query:")
    
    if st.button("Ask"):
        if user_input:
            st.write("#### " + facts[random.randint(0,len(facts)-1)])
            response = chatbotCore.run_chatbot(user_input)  # Call the chatbot function
            st.write("## Bot's Response:")
            st.write("#### " + response)
        else:
            st.warning("Please enter a query before clicking 'Ask'.")

def pdf_reader():
    display_logo()
    st.title("📖 PDF Reader!")
    st.write("This is the PDF reader!")
    st.write("Here, you can upload any PDF of yours and ask questions regarding it!")

def mobile_device():
    display_logo()
    st.title("Mobile Device Feature")
    st.write("This is the Mobile Device Feature page.")
    st.write("You can use the application on your mobile remote device here.")

def contact_page():
    display_logo()
    st.title("Contact Page")
    st.write("Contact us at contact@example.com")

# Page navigation logic
if menu == "Home":
    home_page()
elif menu == "ChatBot":
    chatbot_page()
elif menu == "PDF_Reader":
    pdf_reader()
elif menu == "Mobile_Device":
    mobile_device()
elif menu == "Contact":
    contact_page()
