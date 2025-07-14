import streamlit as st
import requests
import os
import json
from datetime import datetime
from dotenv import load_dotenv
from base64 import b64encode
from streamlit_extras.stylable_container import stylable_container

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Groq API configuration
API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "llama3-8b-8192"

headers = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

# Set Streamlit page config
st.set_page_config(
    page_title="⚡ Srijan's Personal AI Chatbot",
    page_icon="🤖",
    layout="wide"
)

# Load and encode background image
bg_path = r"C:\Users\Srijan Roy\OneDrive\Documents\openAI chatbot\chatbot image 1.jpg"
with open(bg_path, "rb") as bg_img:
    bg_data = b64encode(bg_img.read()).decode()

st.markdown(f"""
    <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{bg_data}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
    </style>
""", unsafe_allow_html=True)

# Load and encode animated chatbot GIF
gif_path = r"C:\Users\Srijan Roy\OneDrive\Documents\openAI chatbot\Live chatbot.gif"
with open(gif_path, "rb") as gif:
    gif_data = b64encode(gif.read()).decode()

# Load and encode AI logo GIF for footer
footer_gif_path = r"C:\Users\Srijan Roy\OneDrive\Documents\openAI chatbot\AI logo Foriday.gif"
with open(footer_gif_path, "rb") as gif:
    footer_gif_data = b64encode(gif.read()).decode()

# Custom title with animated GIF
st.markdown(f"""
<div style="display: flex; align-items: center; gap: 15px;">
    <img src="data:image/gif;base64,{gif_data}" width="55" height="55">
    <h1 style="margin: 0; color: white;">⚡ Srijan's Personal AI Chatbot</h1>
</div>
<p style="color: white; margin-left: 70px;">Powered by Groq & LLaMA3</p>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("## ⚙️ Settings")
    MODEL = st.selectbox(
        "Choose AI Model",
        ["llama3-8b-8192", "mixtral-8x7b-32768", "gemma-7b-it"],
        index=0
    )

    st.markdown("---")
    st.markdown("### 💾 Chat Tools")

    if "messages" in st.session_state and len(st.session_state.messages) > 1:
        chat_json = json.dumps([msg for msg in st.session_state.messages if msg["role"] != "system"], indent=2)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        st.download_button(
            label="Download Chat History",
            data=chat_json,
            file_name=f"srijan_chat_{timestamp}.json",
            mime="application/json",
            use_container_width=True,
            key="download_chat"
        )
    else:
        st.download_button(
            label="Download Chat History",
            data="",
            file_name="chat.json",
            mime="application/json",
            use_container_width=True,
            disabled=True,
            help="No chat history available to download"
        )

    if st.button("Clear Chat", use_container_width=True):
        st.session_state.messages = [{"role": "system", "content": "You are Srijan's helpful AI assistant."}]
        st.rerun()

# Initialize chat
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are Srijan's helpful AI assistant."}]

# Chat display
chat_container = st.container()
with chat_container:
    for i, msg in enumerate(st.session_state.messages[1:]):
        with stylable_container(
            key=f"{msg['role']}_{i}",
            css_styles=f"""
                {{
                    background-color: {'#4a8cff' if msg['role'] == 'user' else 'white'};
                    color: {'white' if msg['role'] == 'user' else '#333'};
                    border-radius: 18px;
                    padding: 15px;
                    margin: {'10px 0 10px auto' if msg['role'] == 'user' else '10px auto 10px 0'};
                    max-width: 80%;
                    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                }}
            """
        ):
            st.markdown(f"**{'You' if msg['role'] == 'user' else 'Srijan\'s AI'}:** {msg['content']}")

# 🎙 Title before input
st.markdown("### 🎙 Speak to your AI")

# Chat input
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input(
        "Type your message...",
        key="input",
        label_visibility="collapsed",
        placeholder="Ask your AI assistant..."
    )
    submitted = st.form_submit_button("Send")

if submitted and user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.spinner("🤖 Thinking..."):
        try:
            response = requests.post(API_URL, headers=headers, json={
                "model": MODEL,
                "messages": st.session_state.messages,
                "temperature": 0.7
            })
            response.raise_for_status()
            reply = response.json()["choices"][0]["message"]["content"]
            st.session_state.messages.append({"role": "assistant", "content": reply})
        except Exception as e:
            st.error(f"Error: {str(e)}")

    st.rerun()

# Insert GIF above the footer
st.markdown(f"""
<div style="text-align: center; margin-top: 40px;">
    <img src="data:image/gif;base64,{footer_gif_data}" width="100" height="100" alt="AI Logo Animation">
</div>
""", unsafe_allow_html=True)

# ========== FOOTER AND SOCIAL ICONS ==========
st.markdown("""
<!-- Font Awesome CDN -->
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">

<style>
    .social-icons-floating {
        position: fixed;
        bottom: 100px;
        right: 20px;
        display: flex;
        flex-direction: column;
        gap: 12px;
        z-index: 9999;
    }
    .social-icons-floating a {
        color: #28a745;
        background: white;
        border: 2px solid #28a745;
        border-radius: 50%;
        width: 44px;
        height: 44px;
        display: flex;
        align-items: center;
        justify-content: center;
        text-decoration: none;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .social-icons-floating a:hover {
        background: #28a745;
        color: white;
        transform: scale(1.1);
    }
    .footer {
        text-align: center;
        margin-top: 80px;
        padding: 20px;
        font-size: 15px;
        color: #fff;
        background: rgba(0, 0, 0, 0.6);
        border-top: 1px solid #ccc;
        font-family: 'Segoe UI', sans-serif;
    }
</style>

<div class="social-icons-floating">
    <a href="https://www.linkedin.com/in/srijan-roy-29bb19256" target="_blank" aria-label="LinkedIn"><i class="fab fa-linkedin-in"></i></a>
    <a href="https://github.com/SrijanRoy12" target="_blank" aria-label="GitHub"><i class="fab fa-github"></i></a>
    <a href="mailto:roysrijan53@gmail.com" target="_blank" aria-label="Email"><i class="fas fa-envelope"></i></a>
    <a href="https://www.instagram.com/its_ur_roy123/" target="_blank" aria-label="Instagram"><i class="fab fa-instagram"></i></a>
    <a href="https://x.com/home" target="_blank" aria-label="Twitter"><i class="fab fa-twitter"></i></a>
</div>

<div class="footer">
    ⚡Crafted with Code 👨‍💻, 🚀Fueled by Innovation🧠 — <strong>Srijan Roy</strong> | CSE @ IEM Kolkata 📍
</div>
""", unsafe_allow_html=True)
