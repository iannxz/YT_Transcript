import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

def configure_gemini():
    """Configura a API Gemini com a chave da API"""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("A chave da API Gemini não foi encontrada")
    
    genai.configure(api_key=api_key)

def generate_summary(text):
    """Gera um resumo em português"""
    try:
        model = genai.GenerativeModel('gemini-2.0-flash')
        response = model.generate_content(
            f"Resuma este texto em 3 parágrafos concisos em português brasileiro:\n\n{text}"
        )
        return response.text
    except Exception as e:
        st.error(f"Erro ao gerar resumo: {str(e)}")
        return None
    
    