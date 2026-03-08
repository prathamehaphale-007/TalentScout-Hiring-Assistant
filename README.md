# 🤖 TalentScout Hiring Assistant

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![LLM](https://img.shields.io/badge/LLM-Llama%203.3-orange)
![Azure](https://img.shields.io/badge/Deployment-Azure-0078D4)

**TalentScout Hiring Assistant** is an AI-powered chatbot designed to automate the initial candidate screening process for recruitment agencies.

The system conducts conversational interviews, collects candidate technical background, dynamically generates technical questions using a Large Language Model, analyzes response sentiment, and stores candidate information for recruiter review.

This project demonstrates how **LLMs can streamline recruitment workflows and reduce manual screening effort.**

---

# 🌟 Key Features

## 🧠 Context-Aware Conversation

The chatbot maintains conversation memory and remembers:

- Candidate name  
- Technology stack  
- Previous responses  

This creates a natural conversational interview experience.

---

## ⚙️ Dynamic Technical Question Generation

Using **Groq Llama 3.3**, the assistant generates customized interview questions based on the candidate’s declared tech stack.

Examples include:

- Python  
- React  
- AWS  
- Data Engineering tools  

Each candidate receives:

- **Conceptual Question**
- **Scenario-Based Question**
- **Tool-Specific Question**

This ensures a balanced technical assessment.

---

## 📊 Sentiment Analysis

Candidate responses are analyzed using **TextBlob**.

The system classifies responses as:

- Positive
- Neutral
- Negative

The sentiment score is displayed in the **Streamlit sidebar** to provide additional insights into candidate communication tone.

---

## 💾 Candidate Data Persistence

Candidate information is automatically stored in a CSV database.

Example file:

`candidates_db.csv`

Stored data includes:

- Candidate name  
- Tech stack  
- Interview responses  
- Sentiment score  

This acts as a lightweight candidate tracking system.

---

## 🛡️ Robust Fail-Safe System

The application includes a **Mock Mode fallback**.

If the Groq API is unavailable:

- The system generates simulated responses
- The UI remains fully functional
- Demonstrations never fail due to API issues

---

## ☁️ Cloud Deployment Ready

The application can be deployed on **Microsoft Azure App Service**, enabling recruiters to access the chatbot through a browser.

---

# 🧱 System Architecture

<p align="center">
  <img src="https://github.com/user-attachments/assets/504dd016-295b-4f20-bed1-6e4f9c2cca10"
       alt="TalentScout System Architecture"
       width="700">
</p>

```
Candidate Interaction  
↓  
Streamlit Chat Interface  
↓  
Conversation Manager  
↓  
LLM Handler (Groq API)  
↓  
Technical Question Generation  
↓  
Sentiment Analysis (TextBlob)  
↓  
Candidate Data Storage (CSV)  
↓  
Recruiter Review  
```
---

# 🛠️ Technology Stack

| Technology | Purpose |
|-----------|--------|
| **Python** | Core application logic |
| **Streamlit** | Interactive chat interface |
| **Groq API** | LLM-powered question generation |
| **TextBlob** | Sentiment analysis |
| **Pandas** | Data storage & processing |
| **Azure App Service** | Cloud deployment |

---

# 📂 Project Structure

```
TalentScout/

talentscout_app.py → Main Streamlit application  

llm_handler.py → Groq API integration & mock fallback  

utils.py → Helper functions (sentiment analysis, storage, regex)

prompts.py → Prompt templates for LLM interaction  

requirements.txt → Project dependencies  

README.md → Documentation  
```
---

# 🚀 Installation & Setup

Follow these steps to run the project locally.

### 1️⃣ Clone the Repository

```
git clone https://github.com/prathamehaphale-007/TalentScout-Hiring-Assistant.git

cd TalentScout-Hiring-Assistant
```
---

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```
---

### 3️⃣ Run the Application

streamlit run talentscout_app.py

The application will open at:

```
http://localhost:8501
```
---

# 🔑 API Configuration

The application supports two modes.

### Option A — Full AI Mode

Enter your **Groq API Key** in the sidebar for full AI-powered responses.

---

### Option B — Mock Mode

Leave the API key empty.

The system will simulate responses for demonstration and UI testing.

---

# 🧠 Prompt Engineering Strategy

The chatbot uses structured prompts to ensure consistent LLM outputs.

**System Role**

Defines the chatbot persona **Scout**, a professional recruitment assistant focused on candidate screening.

**Structured Output**

Prompts instruct the model to generate:

- One conceptual question  
- One scenario-based question  
- One tool-specific question  

This ensures structured technical evaluation.

**Context Injection**

User inputs such as candidate name and tech stack are dynamically injected into prompts to create personalized interactions.

---

# ☁️ Deployment (Azure)

This project can be deployed to **Azure App Service**.

### Deployment Steps

1. Create a **Python Web App** on Azure  
2. Connect your **GitHub repository** through Deployment Center  
3. Configure the startup command  

Startup command:

```
python -m streamlit run talentscout_app.py --server.port 8000 --server.address 0.0.0.0
```
---

# 🛡️ Challenges & Solutions

### Challenge  
LLM occasionally generated generic interview questions.

### Solution  
Improved prompts to explicitly request:

- One conceptual question  
- One scenario-based question  
- One tool-specific question  

This significantly improved question quality.

---

### Challenge  
Managing conversation flow in the chatbot.

### Solution  
Implemented a **state-machine workflow** guiding interaction stages:

gather_name → gather_stack → interview → evaluation

---

### Challenge  
High API usage during development.

### Solution  
Implemented **Mock Mode** to simulate responses without making API calls.

---

# 👨‍💻 Author

**Prathmesh Aphale**

AI Engineering • Data Science • Intelligent Systems

---

# ⭐ Support

If you found this project useful, consider giving the repository a **star ⭐**.
