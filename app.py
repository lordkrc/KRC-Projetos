import streamlit as st
import streamlit.components.v1 as components

# Configuração da página para ocupar a tela toda
st.set_page_config(layout="wide")

# Opcional: Adicionar um título do Streamlit acima do seu HTML


# Função para ler o seu arquivo HTML original
def carregar_html():
    with open("index.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    return html_content

# No seu app.py, tente esta alteração:
components.html(carregar_html(), width=1500, height=1800, scrolling=True)