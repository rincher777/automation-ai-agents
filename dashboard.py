import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Configuração da página
st.set_page_config(page_title="Monitor de Preços Dev_Rincher", layout="wide")

st.title("📊 Dashboard de Monitorização de Preços")
st.markdown("Este sistema analisa os dados recolhidos pelo **Scraper de Concorrência**.")

# Verificar se o arquivo CSV existe
if os.path.exists('precos_concorrencia.csv'):
    # Carregar dados
    df = pd.read_csv('precos_concorrencia.csv')
    
    # Converter a coluna Data para o formato correto
    df['Data'] = pd.to_datetime(df['Data'], dayfirst=True)
    
    # Sidebar para filtros
    st.sidebar.header("Filtros")
    produto_selecionado = st.sidebar.selectbox("Selecione o Produto", df['Produto'].unique())
    
    df_filtrado = df[df['Produto'] == produto_selecionado]

    # Métricas Principais
    col1, col2 = st.columns(2)
    with col1:
        ultimo_preco = df_filtrado['Preço'].iloc[-1]
        st.metric("Preço Atual", f"R$ {ultimo_preco}")
    
    # Gráfico de Evolução de Preços
    st.subheader(f"Variação de Preço: {produto_selecionado}")
    fig = px.line(df_filtrado, x='Data', y='Preço', markers=True, title="Histórico de Preços")
    st.plotly_chart(fig, use_container_width=True)

    # Exibir a tabela de dados
    st.subheader("Dados Brutos (Logs)")
    st.dataframe(df_filtrado, use_container_width=True)

else:
    st.error("Arquivo 'precos_concorrencia.csv' não encontrado. Execute o scraper primeiro!")