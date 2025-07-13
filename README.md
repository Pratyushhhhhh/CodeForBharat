# ⚖️ CodeForBharat — Legal AI Assistant (RAG Model)

An AI-powered multi-domain legal assistant built for the **Code for Bharat Hackathon**. This system delivers **accurate, simplified legal information** using a **Retrieval Augmented Generation (RAG)** model trained on Indian law.

## ❗ Problem We Are Solving

Millions of Indians struggle to access legal help due to:
* Complex and inaccessible legal language
* Low legal literacy
* Limited access to affordable lawyers

🔍 **Our solution** brings trustworthy, domain-specific legal information to citizens through **voice** and **messaging platforms**, ensuring accessibility for all.

## ✅ What's Working

* ✅ **RAG Model** (fully functional)
* 📚 Trained on:
   * Indian Penal Code (IPC)
   * Right to Information (RTI)
   * Labour Laws (Delhi College Book)
   * Constitution of India

## 🚧 Work in Progress

* 🤖 WhatsApp Bot (using Twilio)
* 📞 IVR Phone Support (using Exotel)
* 🌐 Multilingual Support (Hindi and English available; others in progress)

  <img width="1843" height="826" alt="Screenshot 2025-07-13 120049" src="https://github.com/user-attachments/assets/f380fe2d-b1fa-4b6f-9847-3d3cae043422" />


## 🧠 Tech Stack

| Layer | Tools / Frameworks |
|-------|-------------------|
| **Backend** | FastAPI (Python) |
| **RAG + VectorDB** | ChromaDB |
| **LLMs** | Google Gemini / OpenAI |
| **Voice** | Google STT / TTS, Exotel |
| **Messaging** | Twilio (WhatsApp) |
| **Frontend** | Flask (voice input), Streamlit (text UI) |
| **Languages** | Python, JavaScript, Node.js |

## 📁 Project Structure

```
CodeForBharat/
├── rag/                    # FastAPI-based RAG service
├── ingest/                 # Document ingestion and vector indexing
├── whatsapp/               # WhatsApp bot using Twilio
├── ivr/                    # IVR voice server using Exotel
├── web_voice_server/       # Flask-based voice interface
├── data/                   # Legal corpus: IPC, RTI, Labour, Constitution
├── requirements.txt        # Python dependencies
├── .env.example           # Environment variables template
└── README.md              # This file
```

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Pratyushhhhhh/CodeForBharat.git
cd CodeForBharat
```

### 2. Set Up the RAG Model

```bash
cd rag
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python setup_vector_db.py
uvicorn app:app --host 0.0.0.0 --port 8000
```

### 3. Set Up WhatsApp Bot (WIP)

```bash
cd whatsapp
npm install
cp .env.example .env  # Add your Twilio credentials
npm start
```

### 4. Environment Variables

Create a `.env` file in the root directory with:

```env
# API Keys
GOOGLE_API_KEY=your_google_api_key
OPENAI_API_KEY=your_openai_api_key

# Twilio (WhatsApp)
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_token
TWILIO_PHONE_NUMBER=your_twilio_number

# Exotel (IVR)
EXOTEL_API_KEY=your_exotel_key
EXOTEL_API_TOKEN=your_exotel_token
EXOTEL_SUBDOMAIN=your_exotel_subdomain
```

## ▶️ Usage Instructions

### WhatsApp Bot
1. Text the Twilio sandbox number
2. Select legal domain (IPC/RTI/Labour/Constitution)
3. Ask your legal query
4. Receive simplified legal information

### IVR Call System
1. Call the Exotel number
2. Press digit for domain selection
3. Speak your legal query
4. Get voice response with legal guidance

### Web Interface
1. Open the web app
2. Speak your query using voice input
3. Get both voice and text responses

## 🎯 Key Features

* **Domain-Specific Knowledge**: Trained on 4 major Indian legal domains
* **RAG-Powered Accuracy**: Combines retrieval with generation for precise answers
* **Multi-Modal Access**: Voice, text, and messaging support
* **Simplified Language**: Complex legal jargon converted to understandable language
* **Scalable Architecture**: FastAPI backend with ChromaDB vector storage

## 🚀 Future Roadmap

- [ ] 🌍 Full multilingual support (Kannada, Tamil, Bengali, etc.)
- [ ] 📄 Legal document upload with contextual Q&A
- [ ] ⚖️ Lawyer referral system
- [ ] 🔒 User authentication and history tracking
- [ ] 🌐 Public-facing web and mobile apps (chat + voice)
- [ ] 📊 Analytics dashboard for legal query trends
- [ ] 🤝 Integration with government legal portals

## 📈 Impact & Vision

Our vision is to democratize legal access in India by:
* Reducing legal literacy barriers
* Providing 24/7 accessible legal guidance
* Supporting multiple Indian languages
* Bridging the gap between citizens and legal information

## 🏆 Hackathon Achievements

Built for **Code for Bharat Hackathon** with focus on:
* **Social Impact**: Addressing real legal accessibility issues
* **Technical Innovation**: RAG model for legal domain
* **Scalability**: Multi-platform deployment ready
* **User Experience**: Voice and messaging interfaces

## 👥 Team

Built with ❤️ by **Team Heuristic**, Graphic Era Deemed to Be University:

* **Pratyush Bansal** — Team Leader & RAG Model Development
* **Vansh Goyal** — Legal Bot Development (IPC, RTI, Labour, Constitution)

## 📎 Repository

🔗 **GitHub Link**: [https://github.com/Pratyushhhhhh/CodeForBharat](https://github.com/Pratyushhhhhh/CodeForBharat)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.
=

*Making legal information accessible to every Indian citizen* 🇮🇳
