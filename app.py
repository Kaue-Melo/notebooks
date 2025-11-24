import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np


##############################
car_data = pd.read_csv('vehicles.csv')
hist_button = st.button('Mostrar Histograma do Odômetro dos Carros')
if hist_button:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    # criar um histograma
    fig = px.histogram(car_data, x="odometer",
                       title="Distribuição do Odômetro dos Carros")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

###############################
disp_button = st.button(
    'Mostrar Gráfico de Dispersão do Preço do Carro vs. Ano do Modelo')
if disp_button:
    st.write(
        "Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros")

    fig1 = px.scatter(car_data, x="model_year", y="price", color="condition",
                      title="Relação entre Ano do Carro e Preço por Condição")
    st.plotly_chart(fig1, use_container_width=True)
