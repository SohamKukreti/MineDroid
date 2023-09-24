import streamlit as st
import os
import random
from googletrans import Translator
import chatbotCore  # Import the modified chatbotCore module
import pdfbot  # Import the pdfbot module

# st.markdown(page_bg_img, unsafe_allow_html=True)
# st.set_page_config(page_title="Multi-Page Landing", layout="wide")

# Add your logo image file path here
logo_path = "logo.png"

menu = st.sidebar.selectbox("Navigation", ["Home", "ChatBot", "PDF_Reader", "Contact"])

facts = ["fact1", "fact2", "fact3", "fact4", "fact5", "fact6", "fact7", "fact8", "fact9", "fact10", "fact11"]

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
    st.write("### Select your Option from the Sidebar selectbox! 😃 \n--------")
    st.write("### Our Mission:")
    st.write("##### Our mission is to empower individuals, including those without specialized legal knowledge, with easy access to comprehensive information on Indian mining laws, rules, and regulations. Through our website featuring two intelligent chatbots, we aim to simplify the complexities of mining-related inquiries. Our normal chatbot provides real-time, user-friendly responses to queries, while our PDF reader chatbot extracts and summarizes key insights from lengthy legal documents, ensuring that everyone can navigate and understand the intricacies of Indian mining laws effortlessly, ultimately promoting transparency, compliance, and informed decision-making in the mining sector.")
   

def chatbot_page():
    display_logo()
    st.title("🧠 ChatBot Page")
    st.write("This is the Chat_Bot Page. Here, you can ask your queries in any language.")

    # Create a text input field for user queries
    user_input = st.text_input("Enter your query:")

    if st.button("Ask"):
        if user_input:
            st.write("#### " + facts[random.randint(0, len(facts) - 1)])
            response = chatbotCore.run_chatbot(user_input)  # Call the chatbot function
            st.write("## Bot's Response:")
            st.write("#### " + response)
        else:
            st.warning("Please enter a query before clicking 'Ask'.")

def pdf_reader_page():
    display_logo()
    st.title("📖 PDF Reader!")
    st.write("This is the PDF reader!")
    st.write("Here, you can upload any PDF of yours and ask questions regarding it!")

    # Call the pdf_reader function from pdfbot module
    pdfbot.pdf_reader()

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
    pdf_reader_page()
elif menu == "Mobile_Device":
    mobile_device()
elif menu == "Contact":
    contact_page()