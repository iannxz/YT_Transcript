# 📽️ YouTube Video Summarizer com IA

Uma aplicação em Python que transforma vídeos do YouTube em **texto transcrito** e gera **resumos automáticos** utilizando **Inteligência Artificial (Gemini API)**.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?style=flat&logo=python" />
  <img src="https://img.shields.io/badge/Streamlit-App-red?style=flat&logo=streamlit" />
  <img src="https://img.shields.io/badge/Gemini-API-yellow?style=flat&logo=google" />
</p>

---

## ✨ Funcionalidades

✅ Receba uma **URL do YouTube**  
✅ Extraia a **transcrição completa** do vídeo  
✅ Gere automaticamente um **resumo inteligente** com IA  
✅ Interface simples e elegante com **Streamlit**

---

## 🛠️ Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [YouTube Transcript API](https://pypi.org/project/youtube-transcript-api/)
- [Gemini API (Google AI)](https://ai.google.dev/)
- [Pytube](https://pytube.io/)

---

## ▶️ Demonstração

> 🎥 Vídeo demonstrando o app funcionando:  
> *https://github.com/user-attachments/assets/ed0f344b-8924-4b8a-83a1-713d8b902db8*

---

## 🚀 Como executar o projeto

1. Clone o repositório:
bash
git clone https://github.com/iannxz/youtube-transcript.git
cd youtube-transcript

---

📌 Observações
Nem todos os vídeos possuem transcrição pública — a API retornará erro nesses casos.

O resumo depende da qualidade da transcrição.

---

## 📚 Exemplos de Uso
Resumir vídeos longos de aulas ou palestras

Criar sinopses automáticas para vídeos de conteúdo

Transformar vídeos em texto para análise ou revisão

---

## 📁 Estrutura do Projeto
bash
Copiar

https://github.com/user-attachments/assets/0efe3b75-9091-4118-a50a-6b48809bc15f


Editar
YT_translate/
│
├── src/
│   ├── main.py             # App principal (Streamlit)
│   ├── gemini_utils.py     # Funções da API Gemini
│   └── youtube_utils.py    # Transcrição e título
│
├── requirements.txt        # Dependências
├── README.md               # Este arquivo

---

## 💡 Contribuições
Contribuições são bem-vindas!
Sinta-se à vontade para abrir issues, propor melhorias ou enviar PRs 🚀

---

## 📜 Licença
Este projeto está sob a licença MIT.

---

## 🙋‍♂️ Autor
Desenvolvido por Iann Arthur 

