from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi
import streamlit as st

video_url = 'https://www.youtube.com/watch?v=KkCXLABwHP0'

def get_video_title(video_url):
    """Extrai o titulo de um video do YT"""

    try:
        yt = YouTube(video_url)
        return yt.title
    except Exception as e:
        print(f"Erro ao obter o titulo do video: {e}")
        return None
    
def get_transcript(video_id):
    """Obtém a transcrição em português ou traduz do inglês"""
    try:
        # Primeiro tenta obter em português
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['pt'])
            return " ".join([t['text'] for t in transcript])
        except:
            # Se não tiver em português, pega em inglês e traduz
            transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
            english_text = " ".join([t['text'] for t in transcript])
            return translate_to_portuguese(english_text)
    except Exception as e:
        st.error(f"Erro ao obter transcrição: {str(e)}")
        return None

def translate_to_portuguese(text):
    """Traduz texto para português usando Gemini"""
    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(
            f"Traduza este texto para português brasileiro mantendo o significado original:\n\n{text}"
        )
        return response.text
    except Exception as e:
        st.error(f"Erro ao traduzir texto: {str(e)}")
        return None
    
def extract_video_id(url):
    """Extrai o ID do vídeo da URL do YouTube"""
    try:
        yt= YouTube(url)
        return yt.video_id
    except Exception as e:
        print(f"Erro ao extrair o ID do vídeo: {e}")
        return None
    
# Uso das funções
title = get_video_title(video_url)
print(f"Titulo do vídeo: {title}")

video_id = extract_video_id(video_url)
print(f"ID do vídeo: {video_id}")

transcript = get_transcript(video_id)
print(f"Transcrição do video: {transcript}")