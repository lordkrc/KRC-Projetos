import streamlit as st
import pandas as pd

# Configuração da Página
st.set_page_config(page_title="KRC Projetos - Estimador", layout="wide")

# Título e Introdução
st.title("🏗️ KRC Projetos - Estimador Inteligente")

# 1. Explicação da Curva ABC
with st.expander("💡 O que é a Curva ABC? (Clique aqui para ler)"):
    st.markdown("""
    A **Curva ABC** é uma ferramenta estratégica que classifica seus custos por impacto financeiro:
    - 🔴 **Classe A (Alto impacto):** Representa aproximadamente 80% do valor total. Itens vitais que exigem negociação rigorosa.
    - 🟡 **Classe B (Médio impacto):** Representa cerca de 15% do valor total.
    - 🟢 **Classe C (Baixo impacto):** Representa 5% restantes. Itens de menor preocupação orçamentária.
    
    *Use esta métrica para focar suas energias de gestão onde o dinheiro realmente circula.*
    """)

# 2. Painel Lateral de Parâmetros (Substitui o seu Expander de Configurações)
with st.sidebar:
    st.header("⚙️ Painel de Métricas")
    st.caption("Verifique e ajuste os valores antes de calcular")
    
    # Parâmetros de Construção
    st.subheader("Materiais Base")
    p_cimento = st.number_input("Cimento (Saco 50kg)", value=35.00)
    p_areia = st.number_input("Areia Lavada (m³)", value=90.00)
    
    st.subheader("Métricas Técnicas")
    perda_civil = st.slider("Margem de Perda (%)", 0, 20, 10)
    rendimento_bloco = st.number_input("Rendimento Bloco (un/m²)", value=25.0)

# 3. Interface Principal
tab_civil, tab_redes = st.tabs(["🏗️ Construção Civil", "🌐 Infraestrutura de Redes"])

with tab_civil:
    st.subheader("Simulador de Parede (Reboco e Alvenaria)")
    col1, col2 = st.columns(2)
    with col1:
        comprimento = st.number_input("Comprimento (m)", value=8.0)
    with col2:
        altura = st.number_input("Altura (m)", value=2.2)
    
    if st.button("Calcular Estimativa"):
        area = comprimento * altura
        area_com_perda = area * (1 + perda_civil/100)
        
        # Lógica simplificada de custo
        custo_cimento = (area_com_perda * 0.2) * p_cimento
        custo_areia = (area_com_perda * 0.05) * p_areia
        total = custo_cimento + custo_areia
        
        # Exibição de Resultados
        st.success(f"Total Estimado: R$ {total:,.2f}")
        
        # 4. Tabela e Gráfico Curva ABC
        st.subheader("📊 Curva ABC de Impacto")
        df_abc = pd.DataFrame({
            "Insumo": ["Cimento", "Areia", "Mão de Obra"],
            "Custo": [custo_cimento, custo_areia, total * 0.3]
        })
        
        # Ordenando pela maior representatividade (Lógica ABC)
        df_abc = df_abc.sort_values(by="Custo", ascending=False)
        
        st.bar_chart(df_abc.set_index("Insumo"))
        st.dataframe(df_abc)

with tab_redes:
    st.write("Módulo de redes em construção. Utilize a estrutura acima como base.")