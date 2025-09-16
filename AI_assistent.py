# Creating Your Python Programming Assistant in Python

# Import module to interact with the operating system
import os

# Import the Streamlit library to create the interactive web interface
import streamlit as st

# Import the Groq class to connect to the Groq API and access the LLM
from groq import Groq

# Configure the Streamlit page with title, icon, layout, and initial sidebar state
st.set_page_config(
    page_title="DSA AI Coder",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)