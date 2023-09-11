import streamlit as st
from llama_index import VectorStoreIndex, ServiceContext, Document
from llama_index.llms import OpenAI
import openai
from llama_index import SimpleDirectoryReader

from pathlib import Path
from llama_index import download_loader

#PandasExcelReader = download_loader("PandasExcelReader")
#loader = PandasExcelReader()
#documents = loader.load_data(file=Path('dir1/excel.xlsx'), sheet_index=None)

openai.api_key = "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"

st.set_page_config(page_title="Proactive Repair Pal", page_icon="👷‍♀️🛠️", layout="centered", initial_sidebar_state="auto", menu_items=None)
st.title("Proactive Repair Pal👷‍♀️🛠️")
st.divider()
st.markdown("Welcome to the Proactive Repair Pal Bot. I am a proactive repair chatbot that tracks user tasks/complaints with reference IDs, providing real-time updates for enhanced user experience and efficiency")
         
if "messages" not in st.session_state.keys(): # Initialize the chat messages history
    st.session_state.messages = [
        {"role": "assistant", "content": "Ask me about your tasks!"}
    ]

@st.cache_resource(show_spinner=False)
def load_data():
    with st.spinner(text="Loading..."):
        reader = SimpleDirectoryReader(input_dir=" ", recursive=True)
        docs = reader.load_data()
        service_context = ServiceContext.from_defaults(llm=OpenAI(model="gpt-3.5-turbo", temperature=0.5, system_prompt=" "))
        index = VectorStoreIndex.from_documents(docs, service_context=service_context)
        return index

#index = load_data()
# chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True, system_prompt="You are an expert on t.")
#chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True)

if prompt := st.chat_input("Your question"): # Prompt for user input and save to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

for message in st.session_state.messages: # Display the prior chat messages
    with st.chat_message(message["role"]):
        st.write(message["content"])

# If last message is not from assistant, generate a new response
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = chat_engine.chat(prompt)
            st.write(response.response)
            message = {"role": "assistant", "content": response.response}
            st.session_state.messages.append(message) # Add response to message history
