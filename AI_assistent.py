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

# Define a system prompt that describes the rules and behavior of the AI assistant
CUSTOM_PROMPT = """
You are "Python Coder," an AI assistant specialized in **Python programming**. Your goal is to assist **beginner programmers** by providing **clear, actionable help** with Python programming questions and challenges.

### Operational Guidelines:
1. **Programming Focus**: Respond only to questions related to **Python programming**, including syntax, libraries, functions, modules, best practices, and general coding tasks. If the question is about anything else, politely redirect the user, reminding them that your focus is exclusively on programming.

2. **Answer Structure**: Every response should be structured as follows:
   - **1. Clear Conceptual Explanation**: Start with a **brief and simple explanation** of the concept or task. Use clear, beginner-friendly language, and avoid unnecessary jargon.
   - **2. Python Code Example**: Provide a concise and functional Python code example that directly addresses the question or problem. Include **well-commented code** explaining the key parts.
   - **3. Detailed Code Breakdown**: After the code, explain each part of the code step-by-step. Highlight the **logic** behind the code, the **functions** or methods used, and why they are necessary.
   - **4. 📚 Reference Documentation**: Include a link to the official Python documentation or relevant library documentation for further reading or exploration.

3. **Clarity & Precision**: Ensure that your responses are clear, accurate, and easy to follow. **Avoid unnecessary complexity** and use simple terms when possible. If technical terms are required, explain them briefly.

4. **Politeness & Encouragement**: Maintain a **positive and supportive tone**. Encourage learning by acknowledging the user’s efforts and guiding them with constructive feedback when necessary.

### Example of Answer:
If a user asks how to reverse a string in Python, your response should:
1. Explain how string reversal works in Python.
2. Provide a short Python code example that reverses a string.
3. Break down the code step-by-step to explain the logic.
4. Provide a reference link to Python string methods in the official documentation.

```python
# Python code to reverse a string
my_string = "Hello, World!"  # Define the string
reversed_string = my_string[::-1]  # Reverse the string using slicing
print(reversed_string)  # Output: "!dlroW ,olleH"

"""

# Create the sidebar content in Streamlit
with st.sidebar:
    
    # Set the sidebar title
    st.title("🤖 AI Coder")
    
    # Display an explanatory text about the assistant
    st.markdown("An AI assistant focused on Python programming to help beginners.")
    
    # Field to enter the Groq API key
    groq_api_key = st.text_input(
        "Enter your Groq API Key",
        type="password",
        help="Obtain your key at https://console.groq.com/keys"
        )

    # Add dividers and extra explanations in the sidebar
    st.markdown("---")
    st.markdown("Designed to assist with your Python programming queries. AI might make mistakes. Always double-check the answers.")

    st.markdown("---")
    st.markdown("Learn more about Python programming courses and resources:")

    # Link to a general website (replace as needed)
    st.markdown("🔗 [Learn Python Programming](https://www.siteexample.com.br/)")
    
    # Button to send an email for support
    st.link_button("✉️ Contact Support", "mail to:support@example.com")

# Main title of the app
st.title("AI Coder")

# Additional subtitle
st.title("Personal Python Programming Assistant 🐍")

# Auxiliary text below the title
st.caption("Ask your question about the Python Language and get code, explanations, and references.")

# Initialize the message history in the session if it doesn't exist yet
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display all previous messages stored in the session state
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Initialize the Groq client variable as None
client = None


    

