# TalentScout-Hiring-Assistant
![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Groq](https://img.shields.io/badge/AI-Llama%203.3-orange)
![Azure](https://img.shields.io/badge/Deployment-Azure-0078D4)

**TalentScout** is an intelligent chatbot designed to streamline the preliminary candidate screening process for recruitment agencies. By leveraging Large Language Models (LLMs), it engages candidates in a natural conversation to gather essential information and assesses their technical proficiency with dynamically generated questions tailored to their specific tech stack.

## 🌟 Features

* **Context-Aware Conversation:** Maintains memory of the candidate's name and previous inputs for a seamless flow.
* **Dynamic Question Generation:** Uses **Groq Llama 3.3** to create specific technical questions (Conceptual, Scenario-based, & Tool-specific) based on the user's declared tech stack (e.g., Python, React, AWS).
* **📊 Sentiment Analysis (Bonus):** Real-time analysis of the candidate's communication tone (Positive/Neutral/Negative) displayed in the UI sidebar.
* **Data Persistence:** Automatically saves candidate profiles and interview responses to a secure local CSV database (`candidates_db.csv`).
* **Robust Error Handling:** Includes a "Mock Mode" fallback if the API service is unavailable, ensuring the demo never breaks.
* **Cloud Deployment:** Fully deployable to **Microsoft Azure App Service**.

## 🛠️ Tech Stack

* **Frontend:** [Streamlit](https://streamlit.io/) (for a clean, responsive chat interface).
* **LLM Engine:** [Groq API](https://groq.com/) (running Llama-3.3-70b-versatile).
* **Sentiment Analysis:** `TextBlob`.
* **Data Handling:** `pandas` (CSV management).
* **Deployment:** Microsoft Azure.

---

## 🚀 Installation & Setup

Follow these steps to run the application locally.

### Install Dependencies
1.Ensure you have Python installed, then run:

pip install -r requirements.txt
2. Run the Application

streamlit run app.py
The app will open in your browser at http://localhost:8501.

3. API Configuration
Option A (Recommended): Enter your free Groq API Key in the app sidebar for full AI functionality.

Option B: Leave the key blank to use Mock Mode (simulated responses for testing UI flow).

🧠 Prompt Engineering Strategy
The chatbot relies on a modular prompt design (prompts.py) to ensure consistency and quality:

System Role: Defines the persona ("Scout") with strict guidelines to remain professional, empathetic, and focused solely on recruitment.

Structured Output: The TECH_QUESTION_PROMPT is engineered to force the LLM to return exactly three distinct types of questions (Conceptual, Scenario, Tool) to ensure a comprehensive assessment.

Context Injection: User inputs (like name and tech stack) are dynamically injected into prompts to make every interaction feel personalized.

📂 Project Structure
Plaintext

TalentScout/
├── app.py              # Main application entry point (UI & State Management)
├── llm_handler.py      # Logic for Groq API integration & Mock fallback
├── utils.py            # Helper functions (Data saving, Sentiment Analysis, Regex)
├── prompts.py          # Centralized system prompts & templates
├── requirements.txt    # Project dependencies
└── README.md           # Documentation
☁️ Deployment (Azure)
This project is configured for deployment on Azure App Service.

Create Resource: Create a Web App on Azure (Python 3.9).

Deploy Code: Connect your GitHub repository via the Deployment Center.

Startup Command: Configure the startup command in Settings > Configuration:


python -m streamlit run app.py --server.port 8000 --server.address 0.0.0.0
🛡️ Challenges & Solutions
Challenge: The LLM sometimes generated generic questions.

Solution: Refined the prompt to explicitly request "One conceptual, one scenario, and one tool-specific question," significantly improving relevance.

Challenge: Handling conversation flow (e.g., stopping the user from going off-topic).

Solution: Implemented a state-machine logic in app.py that strictly guides the user through the stages (gather_name -> gather_stack -> quiz).

Challenge: API Costs during testing.

Solution: Implemented a "Mock Mode" in llm_handler.py that simulates AI responses without making API calls.
