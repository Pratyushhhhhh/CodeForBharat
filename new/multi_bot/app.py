import os
import streamlit as st
from utils import LegalBotManager
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Page config
st.set_page_config(
    page_title="Legal AI Assistant",
    page_icon="⚖️",
    layout="wide"
)

# --- Custom CSS Styling ---
st.markdown("""
    <style>
        body {
            background-color: #f9f9fc;
            font-family: 'Segoe UI', sans-serif;
        }
        .stButton > button {
            background-color: #4CAF50;
            color: white;
            border: None;
            padding: 0.6em 1.2em;
            font-size: 1em;
            border-radius: 8px;
        }
        .stTextInput > div > input {
            border-radius: 10px;
            padding: 0.5em;
            border: 1px solid #ccc;
        }
        .block-container {
            padding-top: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown("""
    <div style='background-color:#1c1c1c; padding:20px; border-radius:10px;'>
        <h1 style='text-align:center; color:white;'>⚖️ LegEZ - Your Legal AI Assistant</h1>
        <h4 style='text-align:center; color:#cccccc; font-weight:normal;'>
            Ask your legal questions and get domain-specific responses
        </h4>
    </div>
    <hr style='border-top: 1px solid #bbb;'>
""", unsafe_allow_html=True)

# --- Initialize LegalBotManager ---
@st.cache_resource
def initialize_bot_manager():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        st.error("GOOGLE_API_KEY not found in environment variables!")
        st.stop()

    try:
        return LegalBotManager(google_api_key=api_key)
    except Exception as e:
        st.error(f"Error initializing bot manager: {e}")
        st.stop()

bot_manager = initialize_bot_manager()
available_bots = bot_manager.get_available_bots()

if not available_bots:
    st.warning("⚠️ No bots are available. Please run ingestion first.")
    st.stop()

# --- Sidebar Info ---
with st.sidebar:
    st.header("ℹ️ About")
    st.markdown("""
    This assistant supports legal queries from:
    - 📜 Indian Penal Code (IPC)
    - 🏛️ Constitution of India
    - 🧑‍🏭 Labor Laws
    - 📄 RTI Act
    """)

    st.markdown("---")
    st.header("🧾 Usage")
    st.markdown("""
    1. Select a domain-specific bot  
    2. Enter your legal query  
    3. Review the AI's response and citations  
    """)

# --- Main Interface ---
col1, col2 = st.columns([1.2, 2])
with col1:
    selected_bot = st.selectbox("Select Legal Bot", available_bots)

with col2:
    bot_descriptions = {
        "IPC Bot": "Specialized in Indian Penal Code sections and criminal law.",
        "RTI Bot": "Expert in Right to Information Act procedures and rights.",
        "Labor Law Bot": "Focuses on workers’ rights and employment law.",
        "Constitution Bot": "Covers the Constitution, fundamental rights, and governance."
    }
    if selected_bot in bot_descriptions:
        st.info(bot_descriptions[selected_bot])

st.markdown("---")

# --- Query Interface ---
st.subheader(f"📝 Ask {selected_bot}")
query = st.text_input("Enter your legal query:")

if query:
    try:
        with st.spinner("Analyzing your query..."):
            result = bot_manager.query_bot(selected_bot, query)
            st.markdown("## ✅ Answer")
            st.success(result["result"])

            if result.get("source_documents"):
                st.markdown("## 📚 Sources")
                for i, doc in enumerate(result["source_documents"]):
                    source = doc.metadata.get("source", "Unknown")
                    page = doc.metadata.get("page", "N/A")
                    with st.expander(f"📄 Source {i+1}: {source} (Page {page})"):
                        st.write(doc.page_content[:500] + "...")
    except Exception as e:
        st.error(f"❌ Error: {e}")

# --- Footer ---
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Made with ❤️ for legal empowerment ·2025</p>", unsafe_allow_html=True)
