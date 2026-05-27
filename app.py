import streamlit as st
import pandas as pd

# 1. Configuração da Página (Sempre no topo)
st.set_page_config(page_title="KRC Projetos - Estimador", layout="wide")

# 2. Título e Introdução
st.title("🏗️ KRC Projetos - Estimador Inteligente")

# 3. Explicação da Curva ABC
with st.expander("💡 O que é a Curva ABC?"):
    st.markdown("""
    A **Curva ABC** é uma ferramenta estratégica que classifica seus custos por impacto financeiro:
    - 🔴 **Classe A (Alto impacto):** ~80% do valor total. Itens vitais que exigem negociação rigorosa.
    - 🟡 **Classe B (Médio impacto):** ~15% do valor total.
    - 🟢 **Classe C (Baixo impacto):** ~5% restantes.
    """)

# 4. Painel Lateral de Parâmetros
with st.sidebar:
    st.header("⚙️ Painel de Métricas")
    p_cimento = st.number_input("Preço Cimento (Saco 50kg)", value=35.00)
    p_areia = st.number_input("Preço Areia (m³)", value=90.00)
    perda_civil = st.slider("Margem de Perda (%)", 0, 20, 10)

# 5. Interface Principal (Abas)
tab_civil, tab_redes = st.tabs(["🏗️ Construção Civil", "🌐 Infraestrutura de Redes"])

with tab_civil:
    st.subheader("Simulador de Parede")
    col1, col2 = st.columns(2)
    with col1:
        comprimento = st.number_input("Comprimento (m)", value=8.0)
    with col2:
        altura = st.number_input("Altura (m)", value=2.2)
    
    if st.button("Calcular Estimativa"):
        area = comprimento * altura
        area_com_perda = area * (1 + perda_civil/100)
        
        # Cálculos base
        custo_cimento = (area_com_perda * 0.2) * p_cimento
        custo_areia = (area_com_perda * 0.05) * p_areia
        mao_obra = (area * 50.00) # Exemplo de custo fixo por m2
        
        total = custo_cimento + custo_areia + mao_obra
        
        # Resultados
        st.success(f"Total Estimado: R$ {total:,.2f}")
        
        # Curva ABC
        st.subheader("📊 Curva ABC de Impacto")
        df_abc = pd.DataFrame({
            "Insumo": ["Cimento", "Areia", "Mão de Obra"],
            "Custo": [custo_cimento, custo_areia, mao_obra]
        }).sort_values(by="Custo", ascending=False)
        
        st.bar_chart(df_abc.set_index("Insumo"))
        st.table(df_abc)

with tab_redes:
    st.write("Módulo de infraestrutura de rede em desenvolvimento.")