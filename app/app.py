import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente
load_dotenv()
POSTGRES_URL = os.getenv("POSTGRES_URL")
engine = create_engine(POSTGRES_URL)

def ler_dados_postgres():
    """Lê os dados do banco PostgreSQL e retorna como DataFrame."""
    try:
        with engine.connect() as conn:
            query = text("SELECT * FROM bitcoin_precos ORDER BY timestamp DESC")
            df = pd.read_sql(query, conn)
        return df
    except Exception as e:
        st.error(f"Erro ao conectar no PostgreSQL: {e}")
        return pd.DataFrame()

st.set_page_config(page_title="Dashboard Completo de Engenharia de Dados", layout="wide")
st.title("🚀 Quick Starter Streamlit - Jornada de Dados")

st.header("1. Contexto de Data Engineering")
st.write("""
Esse dashboard simula elementos chave da Engenharia de Dados:
- Coleta/Extração de dados
- Transformação e limpeza
- Visualização de métricas
- Monitoramento de pipelines
""")

st.header("2. Parâmetros para Pipelines")
nome_pipeline = st.text_input("Nome da Pipeline de Dados", value="Pipeline_Ingestao_Bitcoin")
batch_size = st.number_input("Batch size (linhas por ingestão):", min_value=100, max_value=100000, value=1000, step=100)
latencia_maxima = st.slider("Latência Máxima Aceitável (segundos):", min_value=1, max_value=30, value=5)
tipo_pipeline = st.selectbox("Tipo de Pipeline:", ["Batch", "Streaming", "Lambda", "Kappa"])
camadas = st.multiselect("Camadas do pipeline:", ["Raw", "Staging", "Trusted", "Analytics"], default=["Raw", "Staging"])
ativar_logs = st.checkbox("Ativar Logs de Execução")

st.header("3. Dados do Bitcoin (via PostgreSQL)")
df = ler_dados_postgres()
if not df.empty:
    st.subheader("📋 Dados Recentes")
    st.dataframe(df)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.sort_values(by='timestamp')
    st.subheader("📈 Evolução do Preço do Bitcoin")
    st.line_chart(data=df, x='timestamp', y='valor', use_container_width=True)
    st.subheader("🔢 Estatísticas Gerais")
    col1, col2, col3 = st.columns(3)
    col1.metric("Preço Atual", f"${df['valor'].iloc[-1]:,.2f}")
    col2.metric("Preço Máximo", f"${df['valor'].max():,.2f}")
    col3.metric("Preço Mínimo", f"${df['valor'].min():,.2f}")
else:
    st.warning("Nenhum dado encontrado no banco de dados PostgreSQL.")

st.header("4. Monitoramento de Pipelines")
dados_execucoes = {
    "data_execucao": pd.date_range(end=datetime.now(), periods=5, freq="H"),
    "status": ["Sucesso", "Sucesso", "Falha", "Sucesso", "Sucesso"],
    "linhas_processadas": [1000, 1200, 900, 1500, 1300],
    "tempo_execucao_seg": [4.2, 5.1, 7.8, 3.9, 4.5]
}
df_execucoes = pd.DataFrame(dados_execucoes)
st.subheader("Executões Recentes da Pipeline")
st.dataframe(df_execucoes)
st.subheader("Indicadores de Performance")
col1, col2, col3 = st.columns(3)
col1.metric("Total de Linhas Processadas", f"{df_execucoes['linhas_processadas'].sum():,}")
col2.metric("Execuções com Sucesso", str(df_execucoes['status'].value_counts().get("Sucesso", 0)))
col3.metric("Execuções com Falha", str(df_execucoes['status'].value_counts().get("Falha", 0)))

st.header("5. Visualização de Gráficos")
st.subheader("Linhas Processadas por Execução")
st.line_chart(data=df_execucoes, x="data_execucao", y="linhas_processadas")
st.subheader("Tempo de Execução por Data")
st.bar_chart(data=df_execucoes, x="data_execucao", y="tempo_execucao_seg")


if st.button("Disparar Nova Execução"):
    st.info(f"Pipeline '{nome_pipeline}' disparada em modo {tipo_pipeline}.")
    st.write(f"Batch size: {batch_size} linhas. Latência Máxima: {latencia_maxima}s")
    st.write(f"Camadas: {', '.join(camadas)}")

st.markdown("___")
st.caption("Dashboard de Engenharia de Dados com Streamlit e PostgreSQL. © 2024")
