import streamlit as st
from groq import Groq

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="AI Coder",
    page_icon="🐍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─────────────────────────────────────────────
# CUSTOM CSS
# ─────────────────────────────────────────────
st.markdown("""
<style>
    /* Hide default Streamlit header */
    #MainMenu, footer, header { visibility: hidden; }

    /* App background */
    .stApp { background-color: #0d1117; }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #161b22;
        border-right: 1px solid #30363d;
    }

    /* Chat input */
    [data-testid="stChatInput"] textarea {
        background-color: #161b22 !important;
        border: 1px solid #30363d !important;
        color: #e6edf3 !important;
        border-radius: 8px !important;
    }

    /* User message bubble */
    [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {
        background-color: #1c2128;
        border-radius: 10px;
        border: 1px solid #30363d;
        padding: 0.5rem;
        margin-bottom: 0.5rem;
    }

    /* Assistant message bubble */
    [data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]) {
        background-color: #161b22;
        border-radius: 10px;
        border: 1px solid #238636;
        padding: 0.5rem;
        margin-bottom: 0.5rem;
    }

    /* Code blocks */
    code {
        background-color: #161b22 !important;
        border: 1px solid #30363d !important;
        border-radius: 6px !important;
    }

    /* Metric cards */
    [data-testid="stMetric"] {
        background-color: #1c2128;
        border: 1px solid #30363d;
        border-radius: 8px;
        padding: 0.75rem;
    }

    /* Buttons */
    .stButton > button {
        background-color: #238636;
        color: white;
        border: none;
        border-radius: 6px;
        font-weight: 500;
    }
    .stButton > button:hover {
        background-color: #2ea043;
        color: white;
    }

    /* Title styling */
    h1 { color: #e6edf3 !important; }
    h2, h3 { color: #c9d1d9 !important; }
    p, li { color: #8b949e; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# SYSTEM PROMPT
# ─────────────────────────────────────────────
SYSTEM_PROMPT = """
You are "Python Coder," an AI assistant specialized in Python programming.
Your goal is to help beginner programmers with clear, actionable answers.

### Rules:
1. Only answer questions related to Python programming — syntax, libraries,
   functions, best practices, and general coding tasks. If the question is
   off-topic, politely redirect the user.

2. Structure every response as:
   - Brief conceptual explanation (beginner-friendly, no jargon)
   - A working Python code example with inline comments
   - Step-by-step breakdown of the code
   - Link to the relevant official documentation

3. Keep answers clear and precise. Use simple language.
   If technical terms are required, explain them briefly.

4. Be encouraging and supportive. Acknowledge the user's effort
   and guide them constructively.
"""

# ─────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []

if "total_questions" not in st.session_state:
    st.session_state.total_questions = 0

# ─────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🐍 AI Coder")
    st.markdown("Your Python programming assistant for beginners.")
    st.markdown("---")

    groq_api_key = st.text_input(
        "Groq API Key",
        type="password",
        placeholder="gsk_...",
        help="Get your free key at https://console.groq.com/keys"
    )

    # Model selector
    model = st.selectbox(
        "Model",
        options=[
            "llama-3.3-70b-versatile",
            "llama-3.1-8b-instant",
            "llama3-8b-8192",
            "gemma2-9b-it"
        ],
        index=0,
        help="llama-3.3-70b-versatile is the most capable model."
    )

    # Temperature slider
    temperature = st.slider(
        "Creativity",
        min_value=0.0,
        max_value=1.0,
        value=0.5,
        step=0.1,
        help="Lower = more precise. Higher = more creative."
    )

    st.markdown("---")

    # Stats
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Questions", st.session_state.total_questions)
    with col2:
        st.metric("Messages", len(st.session_state.messages))

    st.markdown("---")

    # Clear conversation
    if st.button("🗑️ Clear conversation", use_container_width=True):
        st.session_state.messages = []
        st.session_state.total_questions = 0
        st.rerun()

    st.markdown("---")
    st.markdown("#### 📚 Resources")
    st.markdown("🔗 [Official Python Docs](https://docs.python.org/3/)")
    st.markdown("🔗 [Groq Console](https://console.groq.com/keys)")
    st.markdown("🔗 [Learn Python](https://www.learnpython.org/)")

    st.markdown("---")
    st.link_button("✉️ Contact Support", "mailto:support@example.com", use_container_width=True)

    st.markdown(
        "<p style='font-size:11px; color:#484f58; text-align:center;'>"
        "AI Coder — powered by Groq API<br>"
        "Answers may not always be correct.<br>Always verify your code.</p>",
        unsafe_allow_html=True
    )

# ─────────────────────────────────────────────
# MAIN AREA
# ─────────────────────────────────────────────
st.markdown("# 🐍 AI Coder")
st.markdown("**Personal Python Programming Assistant** — Ask anything about Python and get code, explanations, and references.")
st.markdown("---")

# Welcome message when no conversation yet
if not st.session_state.messages:
    st.markdown("""
    <div style='background-color:#161b22; border:1px solid #30363d; border-radius:10px; padding:1.5rem; margin-bottom:1rem;'>
        <h4 style='color:#e6edf3; margin:0 0 0.75rem;'>👋 Welcome! Here are some things you can ask:</h4>
        <ul style='color:#8b949e; margin:0;'>
            <li>How do I reverse a string in Python?</li>
            <li>What is the difference between a list and a tuple?</li>
            <li>How do I read a CSV file with pandas?</li>
            <li>Explain how for loops work in Python.</li>
            <li>How do I handle exceptions with try/except?</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Display conversation history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ─────────────────────────────────────────────
# CHAT INPUT & RESPONSE
# ─────────────────────────────────────────────
if prompt := st.chat_input("Ask your Python question here..."):

    # API key check
    if not groq_api_key:
        st.warning("⚠️ Please enter your Groq API Key in the sidebar to get started.")
        st.stop()

    # Initialize Groq client
    try:
        client = Groq(api_key=groq_api_key)
    except Exception as e:
        st.error(f"❌ Error initializing Groq client: {e}")
        st.stop()

    # Save and display user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.session_state.total_questions += 1

    with st.chat_message("user"):
        st.markdown(prompt)

    # Build messages for API — system prompt + full history
    messages_for_api = [{"role": "system", "content": SYSTEM_PROMPT}]
    for msg in st.session_state.messages:
        messages_for_api.append({"role": msg["role"], "content": msg["content"]})

    # Generate and display assistant response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = client.chat.completions.create(
                    messages=messages_for_api,
                    model=model,
                    temperature=temperature,
                    max_tokens=2048,
                )

                assistant_response = response.choices[0].message.content
                st.markdown(assistant_response)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": assistant_response
                })

            except Exception as e:
                st.error(f"❌ Error communicating with the Groq API: {e}")