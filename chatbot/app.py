from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate # Need for chatbots
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

## LangSmith Tracking Only
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

## ChatPrompt Template

from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a sales assistant for a car finance company. A human has responded positively to a message informing them they have been pre-approved for finance. Your task is to arrange a phone call with the human, who is interested in obtaining finance for their car purchase, and the company specialist adviser. Your goal is to convince the human to have a call with our specialist adviser, who can provide advice and interest rates based on their individual circumstances. Determine availability and book a call as soon as possible, preferably today. Your name is {name}. Finish the chat by confirming the details of the call including time and date"),
        ("ai", "Hi' I'm Nat from We Finance Any Car, Great news, your finance has been approved. Are you still interested?"),
        ("human", "Yes, I am still interested."),
        ("ai", "Great' are you available today for a call with out specialist adviser?"),
        ("human", "Question: {user_input}"),
    ]
)

messages = chat_template.format_messages(name="Nat", user_input="What is your name?")

# messages = chat_template.format_messages(name="Anthony")

## Streamlit Framework

st.title('Langchain Demo With OPENAI API')
input_text=st.text_input("What is your question?")

# openAI LLM 
llm=ChatOpenAI(model="gpt-3.5-turbo")
output_parser=StrOutputParser()
chain=chat_template|llm|output_parser

if input_text:
    st.write(chain.invoke({'user_input':input_text, 'name': "Nat"}))