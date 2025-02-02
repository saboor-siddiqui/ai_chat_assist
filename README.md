# AI Chat Assistant

A modern, user-friendly chat interface powered by DeepSeek-R1-Qwen-32B model, built with Streamlit.

## Features

- 🤖 Interactive chat interface with DeepSeek-R1-Qwen-32B model
- 💬 Real-time message updates
- 🎨 Clean and modern UI design
- ⏰ Message timestamps
- 🗑️ Chat history clearing functionality
- 🔐 Secure API key handling

## Prerequisites

- Python 3.7+
- Streamlit
- Krutrim Cloud API key

## Installation

1. Clone the repository:
```bash
git clone git@github.com:saboor-siddiqui/ai_chat_assist.git
```
Install the required dependencies:
```bash
pip install -r requirements.txt
```
Create a .env file in the project root and add your Krutrim Cloud API key:
```
KRUTRIM_CLOUD_API_KEY=your_api_key_here
```

Start the application:
```bash
streamlit run app.py
```