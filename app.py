import streamlit as st
import requests
from dotenv import load_dotenv
import os
from datetime import datetime

# Load environment variables and setup
load_dotenv()
api_key = os.getenv('KRUTRIM_CLOUD_API_KEY')

# Page configuration
st.set_page_config(page_title="AI Chat Assistant", layout="wide")

# Enhanced Custom CSS
st.markdown("""
    <style>
    .stTextArea textarea {
        border-radius: 15px;
        border: 1px solid #4a4a4a;
        background-color: #2b2b2b;
        font-size: 16px;
        padding: 15px;
    }
    .chat-message {
        padding: 1.5rem;
        border-radius: 15px;
        margin-bottom: 1rem;
        display: flex;
        flex-direction: column;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }
    .user-message {
        background-color: #2b2b2b;
        margin-left: 2rem;
    }
    .assistant-message {
        background-color: #1e1e1e;
        margin-right: 2rem;
        border-left: 4px solid #666;
    }
    .timestamp {
        color: #888;
        font-size: 0.8rem;
        margin-bottom: 0.5rem;
        font-style: italic;
    }
    .stButton button {
        border-radius: 10px;
        padding: 0.5rem 1rem;
        background-color: #444;
        color: white;
        border: none;
        transition: all 0.3s ease;
    }
    .stButton button:hover {
        background-color: #666;
        transform: translateY(-2px);
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state for chat history
if 'messages' not in st.session_state:
    st.session_state.messages = []

def main():
    # Header
    col1, col2 = st.columns([3, 1])
    with col1:
        st.title("🤖 AI Chat Assistant")
    with col2:
        st.caption("Using DeepSeek-R1-Qwen-32B")
    
    # Chat history display
    for message in st.session_state.messages:
        with st.container():
            message_type = "user-message" if message["role"] == "user" else "assistant-message"
            st.markdown(f"""
                <div class="chat-message {message_type}">
                    <div class="timestamp">{message["timestamp"]}</div>
                    <div>{message["content"]}</div>
                </div>
            """, unsafe_allow_html=True)

    # User input section
    with st.container():
        user_query = st.text_area("", placeholder="Type your message here...", height=100)
        col1, col2, col3 = st.columns([6, 1, 1])
        with col2:
            send_button = st.button("Send 📤", use_container_width=True)
        with col3:
            clear_button = st.button("Clear 🗑️", use_container_width=True)

    if send_button and user_query:
        # Add user message to chat history
        st.session_state.messages.append({
            "role": "user",
            "content": user_query,
            "timestamp": datetime.now().strftime("%H:%M")
        })

        try:
            # API call
            response = requests.post(
                "https://cloud.olakrutrim.com/v1/chat/completions",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {api_key}"
                },
                json={
                    "model": "DeepSeek-R1-Qwen-32B",
                    "messages": [{"role": "user", "content": user_query}]
                }
            )
            response.raise_for_status()
            
            # Add assistant response to chat history
            assistant_response = response.json().get('choices', [{}])[0].get('message', {}).get('content', '')
            st.session_state.messages.append({
                "role": "assistant",
                "content": assistant_response,
                "timestamp": datetime.now().strftime("%H:%M")
            })
            
            # Rerun to update the chat display
            # Replace experimental_rerun with rerun
            st.rerun()
            
        except Exception as exc:
            st.error(f"Error: {exc}")

    if clear_button:
        st.session_state.messages = []
        st.rerun()

if __name__ == "__main__":
    main()