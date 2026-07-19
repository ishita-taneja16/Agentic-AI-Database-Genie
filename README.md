# 🤖 Agentic AI Database Genie

An AI-powered database assistant that enables users to query structured housing data using natural language. The system converts user queries into SQL, executes them on a SQLite database, and returns intelligent, human-readable responses using Google's Gemini API.

---

## 🚀 Features

- 💬 Natural Language to SQL conversion
- 🧠 AI-powered query understanding using Google Gemini
- 🗄️ SQLite database integration
- 📊 Housing dataset analysis
- ⚡ Fast and interactive Streamlit interface
- 🔍 Automatic database querying
- 📈 Intelligent response generation

---

# 🛠️ Tech Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,sqlite,vscode,git,github" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Google-Gemini_API-4285F4?style=for-the-badge&logo=google&logoColor=white"/>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"/>
</p>

---

## 📂 Project Structure

```text
Agentic-AI-Database-Genie/
│
├── app.py                 # Main application
├── ui.py                  # Streamlit UI
├── ai_query.py            # Gemini API & SQL generation
├── database.py            # Database utilities
├── load_data.py           # CSV to SQLite loader
├── check_models.py        # Model checker
├── train_final.csv        # Housing dataset
├── houses.db              # Generated SQLite database
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/ishita-taneja16/Agentic-AI-Database-Genie.git
cd Agentic-AI-Database-Genie
```

### Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure API Key

Create a `.env` file.

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

---

## 📥 Load Dataset

```bash
python load_data.py
```

---

## ▶️ Run Application

```bash
streamlit run ui.py
```

---

## 💡 Example Queries

- Show houses under ₹50 Lakhs
- Which city has the highest average house price?
- Find properties with more than 3 bedrooms.
- Show houses with parking.
- Average price by locality.
- Houses near schools.

---

## 📸 Application Workflow

```text
User Question
      │
      ▼
Streamlit UI
      │
      ▼
Gemini API
      │
      ▼
Generate SQL Query
      │
      ▼
SQLite Database
      │
      ▼
Query Results
      │
      ▼
AI Generated Response
```

---

## 🔮 Future Enhancements

- Agentic AI using LangGraph
- PostgreSQL Support
- MySQL Support
- Voice-based Database Querying
- Data Visualization Dashboard
- Multi-Database Connectivity
- RAG-powered Knowledge Base

---

## 👩‍💻 Author

**Ishita Taneja**

AI Engineer | Generative AI | Python | LLM | Agentic AI

GitHub:
https://github.com/ishita-taneja16

LinkedIn:
https://linkedin.com/in/ishita-taneja16

---
⭐ If you like this project, don't forget to Star the repository!
