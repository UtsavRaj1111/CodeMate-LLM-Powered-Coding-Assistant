# 🤖 CodeMate — LLM Powered Coding Assistant

CodeMate is an **AI-powered coding mentor** designed to help developers and students **understand programming concepts instead of directly giving full solutions**.

Unlike typical AI chatbots, CodeMate focuses on **guiding the user through logical thinking and problem solving**, making it a great learning companion for coding practice.

---

# 🚀 Live Overview

CodeMate provides a **ChatGPT-style interface** where users can ask coding questions and receive:

* step-by-step hints
* debugging guidance
* conceptual explanations
* beginner-friendly learning support

The application is built using **Streamlit + LangChain + Groq LLMs**, providing **fast inference and a smooth UI experience**.

---

# 🧠 Key Features

✨ **Coding Mentor Mode**
Instead of giving full answers, the assistant provides hints and logical guidance.

⚡ **Ultra Fast Responses**
Powered by **Groq's LLaMA-3 models** for low latency responses.

💬 **ChatGPT Style Interface**
Built using **Streamlit chat components**.

🧠 **Context Aware Conversation**
Maintains chat history for better explanations.

📚 **Beginner Friendly Explanations**
Simplifies programming concepts for learners.

🔐 **Secure API Management**
API keys stored using environment variables.

---

# 🛠️ Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### AI Framework

* LangChain

### LLM Provider

* Groq

### Model

* LLaMA-3 70B

### Environment

* Python Dotenv

---

# 📂 Project Structure

```
CodeMate-LLM-Powered-Coding-Assistant
│
├── app.py                # Main Streamlit application
├── config.py             # Configuration and environment variables
├── llm.py                # LLM initialization
├── prompts.py            # System prompts
├── utils.py              # Helper functions
│
├── requirements.txt      # Project dependencies
├── .env                  # API keys (not uploaded to GitHub)
│
└── components/
    └── chat_ui.py        # Chat interface components
```

---

# ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/UtsavRaj1111/CodeMate-LLM-Powered-Coding-Assistant.git
cd CodeMate-LLM-Powered-Coding-Assistant
```

---

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 3️⃣ Create environment file

Create a `.env` file in the root directory.

```
GROQ_API_KEY=your_groq_api_key_here
```

---

### 4️⃣ Run the application

```
streamlit run app.py
```

---

# 🖥️ Application Interface

The application includes:

### Sidebar

* Model configuration
* Tech stack overview
* Features description

### Chat Interface

* Ask coding questions
* Receive hints and explanations
* Maintain conversation context

---

# 🔒 Security

Sensitive information such as API keys are **stored in `.env` files** and excluded from version control using `.gitignore`.

---

# 🎯 Use Cases

CodeMate can be used for:

* Learning programming concepts
* Understanding coding logic
* Debugging beginner mistakes
* Practicing algorithmic thinking
* Improving problem solving skills

---

# 🚀 Future Improvements

Planned enhancements include:

* Streaming responses (typing effect)
* Code execution sandbox
* Multiple AI modes (Debug / Explain / Optimize)
* File upload for code analysis
* Deployment on Streamlit Cloud

---

# 👨‍💻 Author

**Utsav Raj**

AI / ML Enthusiast & Developer

GitHub:
https://github.com/UtsavRaj1111

---

# ⭐ Support

If you found this project useful, consider **starring the repository** to support the project.
