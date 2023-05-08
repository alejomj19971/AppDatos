import streamlit as st    
from PIL import Image

 
st.title("Análisis de Datos")


st.markdown('Aquí encontrara análisis de datos de Accidentes de Movilidad en Medellín, y de la Esperanza de Vida de los años a 2015')

st.markdown('Visite estos reportes usando la barra lateral e interactue con los distintos filtros')


image = Image.open('graficas.png')

st.image(image, caption='Analisis de Datos')