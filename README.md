# 📚 AI Study Assistant

An interactive Generative AI web application built with **Python**, **Streamlit**, and **Microsoft Azure AI Foundry** that transforms lengthy lecture notes into structured, exam-ready study guides.

## ✨ Features
- **Instant Study Material Generation:** Converts raw notes into key points, definitions, summaries, and revision aids.
- **Microsoft Azure AI Foundry Integration:** Uses the **Azure AI Model Inference API** (`Chat Completions`) for cloud-hosted LLM inference.
- **Interactive AI Controls:** Customize **Temperature**, **Top-p (Nucleus Sampling)**, and **Max Response Tokens** directly from the sidebar.
- **Offline Simulation Mode:** Built-in local fallback engine so the app runs smoothly without internet access or active cloud credentials.

## 🛠️ Tech Stack
- **Frontend:** Streamlit (Python)
- **AI Platform:** Microsoft Azure AI Foundry (`azure-ai-inference`)
- **Prompt Engineering:** Modular system & user prompt templates (`prompts.py`)

## 🚀 How to Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com
   cd ai-study-assistant
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   streamlit run app.py
   ```
