from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')

# Prompt template

prompt = ChatPromptTemplate(
    [("system":"You are a helpful assistant. Please respond to the user querries"),
     ("user":"Question: {question}")   
    ]
)

# Streamlid framework
st.title("LANGCHAIN demo with OPEN AI API")
input_text = st.text_input("Search the topic you want")


