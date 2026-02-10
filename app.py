import streamlit as st
import pandas as pd
import plotly.express as px

# ler os dados
car_data = pd.read_csv('vehicles.csv')

# cabeçalho principal
st.header('Dashboard de Vendas de Carros')

hist_checkbox = st.checkbox('Criar histograma')
scatter_checkbox = st.checkbox('Criar gráfico de dispersão')

# Depois verificar as condições
if hist_checkbox:
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

if scatter_checkbox:
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
            