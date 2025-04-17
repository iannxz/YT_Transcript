import sys
import os
import time
import streamlit as st
from pytube import YouTube
import youtube_utils
import gemini_utils
from streamlit.components.v1 import html

# Configuração de página minimalista
st.set_page_config(
    page_title="YouTube AI Summarizer",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# CSS personalizado com animações
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&display=swap');
    
    :root {{
        --primary: #6C63FF;
        --secondary: #4A90E2;
        --accent: #FF6584;
    }}
    
    html, body, [class*="css"] {{
        font-family: 'Montserrat', sans-serif;
        background-color: #0F172A;
        color: #F8FAFC;
    }}
    
    .main-title {{
        background: linear-gradient(90deg, var(--primary), var(--secondary), var(--accent));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-size: 3rem;
        font-weight: 800;
        margin-bottom: 1.5rem;
        text-shadow: 0 2px 10px rgba(108, 99, 255, 0.3);
        letter-spacing: -1px;
        animation: titleGlow 3s ease-in-out infinite alternate;
    }}
    
    @keyframes titleGlow {{
        0% {{ text-shadow: 0 2px 10px rgba(108, 99, 255, 0.3); }}
        100% {{ text-shadow: 0 2px 20px rgba(255, 101, 132, 0.5); }}
    }}
    
    .input-container {{
        animation: fadeIn 1s ease-out;
        margin-bottom: 2rem;
    }}
    
    @keyframes fadeIn {{
        from {{ opacity: 0; transform: translateY(20px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}
    
    .stTextInput>div>div>input {{
        background-color: rgba(15, 23, 42, 0.7);
        border: 1px solid rgba(74, 144, 226, 0.3);
        border-radius: 12px;
        padding: 15px;
        color: white;
        font-size: 1rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }}
    
    .stButton>button {{
        background: linear-gradient(135deg, var(--primary) 0%, var(--accent) 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 15px 30px;
        font-weight: 700;
        font-size: 1.1rem;
        box-shadow: 0 4px 15px rgba(108, 99, 255, 0.3);
        transition: all 0.3s;
        width: 100%;
        margin: 1rem 0;
    }}
    
    .stButton>button:hover {{
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(108, 99, 255, 0.4);
    }}
    
    .video-card {{
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.7) 0%, rgba(15, 23, 42, 0.9) 100%);
        border-radius: 16px;
        padding: 2rem;
        margin: 2rem 0;
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.3);
        border: 1px solid rgba(255, 255, 255, 0.05);
        animation: cardAppear 0.8s cubic-bezier(0.22, 1, 0.36, 1);
    }}
    
    @keyframes cardAppear {{
        from {{ opacity: 0; transform: scale(0.9); }}
        to {{ opacity: 1; transform: scale(1); }}
    }}
    
    .success-message {{
        color: #48BB78;
        background-color: rgba(72, 187, 120, 0.1);
        padding: 1.2rem;
        border-radius: 12px;
        border-left: 4px solid #48BB78;
        animation: pulse 2s infinite;
    }}
    
    @keyframes pulse {{
        0% {{ box-shadow: 0 0 0 0 rgba(72, 187, 120, 0.4); }}
        70% {{ box-shadow: 0 0 0 10px rgba(72, 187, 120, 0); }}
        100% {{ box-shadow: 0 0 0 0 rgba(72, 187, 120, 0); }}
    }}
    
    .floating {{
        animation: floating 3s ease-in-out infinite;
    }}
    
    @keyframes floating {{
        0% {{ transform: translateY(0px); }}
        50% {{ transform: translateY(-10px); }}
        100% {{ transform: translateY(0px); }}
    }}
</style>
""", unsafe_allow_html=True)

def typewriter_effect(text, placeholder, speed=30):
    current_text = ""
    for char in text:
        current_text += char
        placeholder.markdown(f'<div style="font-size: 1.5rem; font-weight: 700; margin: 1rem 0;">{current_text}</div>', unsafe_allow_html=True)
        time.sleep(1/speed)

def main():
    # Título principal com animação
    st.markdown('<h1 class="main-title floating">✨ YouTube AI Summarizer</h1>', unsafe_allow_html=True)
    st.caption("Transforme vídeos em insights com IA")
    
    # Container de entrada com animação
    with st.container():
        st.markdown('<div class="input-container">', unsafe_allow_html=True)
        video_url = st.text_input(
            " ",
            "https://www.youtube.com/watch?v=KkCXLABwHP0",
            placeholder="Cole a URL do vídeo do YouTube aqui"
        )
        st.markdown('</div>', unsafe_allow_html=True)
        
        if video_url:
            try:
                with st.spinner("🔍 Analisando o vídeo..."):
                    # Animação de loading
                    progress_bar = st.progress(0)
                    for percent_complete in range(100):
                        time.sleep(0.02)
                        progress_bar.progress(percent_complete + 1)
                    
                    video_id = youtube_utils.extract_video_id(video_url)
                    video_title = youtube_utils.get_video_title(video_url)
                    transcript = youtube_utils.get_transcript(video_id)
                    
                    if video_title:
                        title_placeholder = st.empty()
                        typewriter_effect(f"🎬 {video_title}", title_placeholder)
                    
                    if transcript:
                        with st.expander("📜 VER TRANSCRIÇÃO", expanded=False):
                            st.markdown(f"""
                            <div class="video-card">
                                <div style="font-size: 1rem; line-height: 1.6; color: #E2E8F0;">
                                    {transcript[:2000] + ("..." if len(transcript) > 2000 else "")}
                                </div>
                            </div>
                            """, unsafe_allow_html=True)
                        
                        if st.button("✨ GERAR RESUMO AUTOMÁTICO", type="primary"):
                            with st.spinner("🧠 Processando com IA..."):
                                # Animação de processamento
                                loading_placeholder = st.empty()
                                loading_phrases = ["Analisando conteúdo", "Extraindo insights", "Gerando resumo"]
                                for i in range(9):
                                    loading_placeholder.markdown(f'<div style="text-align: center;">{loading_phrases[i%3]}{"."*(i%3+1)}</div>', unsafe_allow_html=True)
                                    time.sleep(0.3)
                                
                                gemini_utils.configure_gemini()
                                summary = gemini_utils.generate_summary(transcript)
                                
                                if summary:
                                    st.balloons()
                                    st.markdown('<div class="success-message">✅ Resumo gerado com sucesso!</div>', unsafe_allow_html=True)
                                    
                                    # Efeito de digitação no resumo
                                    summary_placeholder = st.empty()
                                    current_summary = ""
                                    for char in summary:
                                        current_summary += char
                                        summary_placeholder.markdown(f"""
                                        <div class="video-card">
                                            <div style="font-size: 1rem; line-height: 1.6; color: #E2E8F0;">{current_summary}</div>
                                        </div>
                                        """, unsafe_allow_html=True)
                                        time.sleep(0.01)
                                else:
                                    st.error("❌ Falha ao gerar o resumo")
                    else:
                        st.error("⚠️ Transcrição não disponível para este vídeo")
                        
            except Exception as e:
                st.error(f"🚨 Erro: {str(e)}")

# No final da função main(), antes do if __name__ == "__main__":

    # Rodapé estilizado
    st.markdown("""
    <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            text-align: center;
            padding: 15px;
            background: rgba(15, 23, 42, 0.7);
            color: #F8FAFC;
            font-family: 'Montserrat', sans-serif;
            font-size: 0.9rem;
            z-index: 100;
            backdrop-filter: blur(5px);
            border-top: 1px solid rgba(255, 255, 255, 0.1);
        }
        .footer-name {
            color: #6C63FF;
            font-weight: 700;
            animation: glow 2s ease-in-out infinite alternate;
        }
        @keyframes glow {
            from { text-shadow: 0 0 5px #6C63FF; }
            to { text-shadow: 0 0 10px #FF6584; }
        }
    </style>
    
    <div class="footer">
        Desenvolvido por <span class="footer-name">IannXz</span> © 2025
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
