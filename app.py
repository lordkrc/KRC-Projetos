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

# Injetando o HTML dentro do app

components.html(carregar_html(), height=1200, scrolling=True)