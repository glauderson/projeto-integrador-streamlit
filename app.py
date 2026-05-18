import streamlit as st
import pandas as pd

# CONFIGURAÇÃO
st.title("🎬 Dashboard Netflix")

st.markdown("""
## Projeto Integrador - Análise de Dados de Streaming

Este dashboard apresenta uma análise de dados da plataforma Netflix, permitindo identificar padrões de produção, distribuição de gêneros, evolução temporal dos títulos e características dos conteúdos disponíveis.

### Objetivos da análise:
- Identificar tendências de conteúdo
- Analisar distribuição por gênero
- Avaliar evolução temporal dos lançamentos
- Verificar países com maior volume de produções
""")

# LER DADOS
df = pd.read_csv("netflix_titles.csv")

# MÉTRICAS
total_titulos = len(df)

filmes = len(df[df['type'] == 'Movie'])

series = len(df[df['type'] == 'TV Show'])

# EXIBIR MÉTRICAS
col1, col2, col3 = st.columns(3)

col1.metric("Total de Títulos", total_titulos)

col2.metric("Filmes", filmes)

col3.metric("Séries", series)

# MOSTRAR DADOS
st.write(df.head())

import plotly.express as px

# CONTAGEM DE FILMES E SÉRIES
tipo_count = df['type'].value_counts().reset_index()

tipo_count.columns = ['Tipo', 'Quantidade']

# GRÁFICO
fig = px.pie(
    tipo_count,
    names='Tipo',
    values='Quantidade',
    title='Filmes vs Séries'
)

# MOSTRAR GRÁFICO
st.plotly_chart(fig)

# GÊNEROS MAIS FREQUENTES

generos = df['listed_in'].str.split(', ').explode()

generos_count = generos.value_counts().head(10).reset_index()

generos_count.columns = ['Gênero', 'Quantidade']

fig_generos = px.bar(
    generos_count,
    x='Gênero',
    y='Quantidade',
    title='Top 10 Gêneros Mais Frequentes'
)

st.plotly_chart(fig_generos)

# EVOLUÇÃO DE LANÇAMENTOS POR ANO

ano_count = df['release_year'].value_counts().sort_index().reset_index()

ano_count.columns = ['Ano', 'Quantidade']

fig_ano = px.line(
    ano_count,
    x='Ano',
    y='Quantidade',
    title='Evolução de Lançamentos por Ano'
)

st.plotly_chart(fig_ano)

# PAÍSES COM MAIS CONTEÚDOS

paises = df['country'].dropna().str.split(', ').explode()

paises_count = paises.value_counts().head(10).reset_index()

paises_count.columns = ['País', 'Quantidade']

fig_paises = px.bar(
    paises_count,
    x='País',
    y='Quantidade',
    title='Top 10 Países com Mais Conteúdo'
)

st.plotly_chart(fig_paises)

# CLASSIFICAÇÕES MAIS FREQUENTES

rating_count = df['rating'].dropna().value_counts().head(10).reset_index()

rating_count.columns = ['Classificação', 'Quantidade']

fig_rating = px.bar(
    rating_count,
    x='Classificação',
    y='Quantidade',
    title='Classificações Indicativas Mais Frequentes'
)

st.plotly_chart(fig_rating)

