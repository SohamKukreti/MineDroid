import streamlit as st
import os
import random
from googletrans import Translator
import chatbotCore  # Import the modified chatbotCore module

page_bg_img = """
<style>

    [data-testid="stAppViewContainer"]{
    
    font-family: 'Share Tech', sans-serif;
    font-size: 35px;
    color: white;
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 0;
    width: 100vw;
    height: 100vh;
    text-shadow: 8px 8px 10px #0000008c;
    background-color: #343a40;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='28' height='49' viewBox='0 0 28 49'%3E%3Cg fill-rule='evenodd'%3E%3Cg id='hexagons' fill='%239C92AC' fill-opacity='0.25' fill-rule='nonzero'%3E%3Cpath d='M13.99 9.25l13 7.5v15l-13 7.5L1 31.75v-15l12.99-7.5zM3 17.9v12.7l10.99 6.34 11-6.35V17.9l-11-6.34L3 17.9zM0 15l12.98-7.5V0h-2v6.35L0 12.69v2.3zm0 18.5L12.98 41v8h-2v-6.85L0 35.81v-2.3zM15 0v7.5L27.99 15H28v-2.31h-.01L17 6.35V0h-2zm0 49v-8l12.99-7.5H28v2.31h-.01L17 42.15V49h-2z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E"), linear-gradient(to right top, #343a40, #2b2c31, #211f22, #151314, #000000);

    button {
 --border-radius: 15px;
 --border-width: 4px;
 appearance: none;
 position: relative;
 padding: 1em 2em;
 border: 0;
 background-color: #212121;
 font-family: "Roboto", Arial, "Segoe UI", sans-serif;
 font-size: 18px;
 font-weight: 500;
 color: #ffffff;
 z-index: 2;
}

button::after {
 --m-i: linear-gradient(#000, #000);
 --m-o: content-box, padding-box;
 content: "";
 position: absolute;
 left: 0;
 top: 0;
 width: 100%;
 height: 100%;
 padding: var(--border-width);
 border-radius: var(--border-radius);
 background-image: conic-gradient(
		#488cfb,
		#29dbbc,
		#ddf505,
		#ff9f0e,
		#e440bb,
		#655adc,
		#488cfb
	);
 -webkit-mask-image: var(--m-i), var(--m-i);
 mask-image: var(--m-i), var(--m-i);
 -webkit-mask-origin: var(--m-o);
 mask-origin: var(--m-o);
 -webkit-mask-clip: var(--m-o);
 mask-composite: exclude;
 -webkit-mask-composite: destination-out;
 filter: hue-rotate(0);
 animation: rotate-hue linear 500ms infinite;
 animation-play-state: paused;
}

button:hover::after {
 animation-play-state: running;
}

@keyframes rotate-hue {
 to {
  filter: hue-rotate(1turn);
 }
}

button,
button::after {
 box-sizing: border-box;
}

button:active {
 --border-width: 5px;
}
}
 
   
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
#st.set_page_config(page_title="Multi-Page Landing", layout="wide")

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
