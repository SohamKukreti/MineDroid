import streamlit as st
import os
import openai
from googletrans import Translator
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.vectorstores import Chroma
import constants

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = constants.APIKEY

# Load or create the index
PERSIST = False
if PERSIST and os.path.exists("persist"):
    st.write("Reusing index...\n")
    vectorstore = Chroma(persist_directory="persist", embedding_function=OpenAIEmbeddings())
    index = VectorStoreIndexWrapper(vectorstore=vectorstore)
else:
    loader = TextLoader("data/data.txt")  # Use this line if you only need data.txt
    if PERSIST:
        index = VectorstoreIndexCreator(vectorstore_kwargs={"persist_directory": "persist"}).from_loaders([loader])
    else:
        index = VectorstoreIndexCreator().from_loaders([loader])

# Create the conversation retrieval chain
chain = ConversationalRetrievalChain.from_llm(
    llm=ChatOpenAI(model="gpt-3.5-turbo"),
    retriever=index.vectorstore.as_retriever(search_kwargs={"k": 1}),
)

# Initialize chat history
chat_history = []

# Function to run the module
def run_module(s):
    global chat_history
    result = chain({"question": s, "chat_history": chat_history})
    chat_history.append((s, result['answer']))
    return result['answer']

def main():
    st.title(" :brain: MineDroid :brain:")

    # Text input field
    text_input = st.text_area("Enter any query you have:")
    
    if st.button("Answer!"):
        translator = Translator()
        detected_lang = translator.detect(text_input).lang
        translated = translator.translate(text_input, dest='en')
        output_text = run_module(translated.text)
        translated_output = translator.translate(output_text, dest=detected_lang).text
        
        # Display the processed text
        st.write("Processed Text:")
        st.write(translated_output)

if __name__ == "__main__":
    main()