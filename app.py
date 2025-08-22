import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')

st.header('Histograma vehiculos')
hist_button = st.button('Construir histograma')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

st.header('Grafico Dispersion  vehiculos')
dis_button = st.button('Construir dispersion')  # crear un botón

if dis_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de dispersion para el conjunto de datos de anuncios de venta de coches')

    # crear grafico de dispersion
    fig2 = px.scatter(car_data, x="odometer", y="price")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig2, use_container_width=True)
