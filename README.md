# ⚡ Srijan's Personal AI Chatbot 🤖

Welcome to **Srijan's Personal AI Chatbot** — a modern, personalized conversational AI interface powered by **Groq** and **LLaMA3**, built with **Streamlit**.

This chatbot combines powerful language modeling with a beautiful, customizable UI. It's designed to deliver a natural, responsive, and engaging chat experience for users.

---

## 🚀 Features

- 💬 **Chat in Real Time** – AI-powered responses using Groq’s LLaMA3 model.
- 🎙 **Voice-Ready UI** – Styled to support future voice integration.
- 🟢 **Modern Chat UI** – Chat bubbles with avatars, custom themes, and animations.
- 🌌 **Background Image & Animated GIFs** – Personal visual branding.
- 💾 **Download Chat History** – Export chats in JSON format.
- 🧹 **Clear Chat Option** – Reset the conversation in one click.
- 🌐 **Floating Social Media Icons** – Quick links to your personal profiles.
- 📎 **Save/Load Conversations** – Easy history handling (optional).

---

## 🛠️ Tech Stack

| Component   | Tech Used                     |
|-------------|-------------------------------|
| Frontend    | Streamlit (Python-based UI)   |
| Backend     | Groq API (`llama3-8b-8192`)   |
| Styling     | Custom CSS, Font Awesome      |
| Hosting     | Localhost / Streamlit Cloud   |

---

## 📦 Installation

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/srijan-chatbot.git
cd srijan-chatbot


2. Set up virtual environment (optional but recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Add your .env file
Create a file named .env with your Groq API key:

ini
Copy
Edit
GROQ_API_KEY=your_groq_api_key_here
▶️ Run the App
bash
Copy
Edit
streamlit run app.py
🔐 Environment Variables
Variable	Description
GROQ_API_KEY	Your Groq.com API key

📂 Folder Structure
arduino
Copy
Edit
📁 srijan-chatbot/
│
├── app.py
├── .env
├── requirements.txt
├── assets/
│   ├── chatbot image 1.jpg
│   ├── Live chatbot.gif
│   └── AI logo Foriday.gif
└── README.md
📬 Contact
Made with ❤️ by Srijan Roy
📧 roysrijan53@gmail.com
🌐 LinkedIn | GitHub | Instagram
