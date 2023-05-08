import streamlit as st
import pandas as pd
import numpy as np


#Title sirve para mostrar un titulo con un texto como parámetro
st.title("Esperanza de Vida (2000-2015) ")

# se lee el archivo en data,queda en un formato de texto compatible para crear un dataframe
data = pd.read_csv('aVida.csv')
df = pd.DataFrame(data)


st.write(df)

pais = st.selectbox('PAIS',(df["Country"].sort_values(ascending=True).unique()))
region = st.selectbox('REGION',(df["Region"].sort_values(ascending=True).unique()))
año = st.selectbox('AÑO',(df["Year"].sort_values(ascending=True).unique()))  
Muerte_de_Infantes = st.selectbox('MUERTE DE INFANTES',(df["Infant_deaths"].sort_values(ascending=True).unique()))  
Mortalidad_en_Adultos = st.selectbox('MORTALIDAD_ADULTOS',(df["Adult_mortality"].sort_values(ascending=True).unique()))  
pib = st.selectbox('PIB',(df["GDP_per_capita"].sort_values(ascending=True).unique()))  
Esperanza_de_Vida= st.selectbox('ESPERANZA DE VIDA',(df["Life_expectancy"].sort_values(ascending=True).unique())) 

#Filtro de barras el loc devuelve un nuevo dataframe con los datos filtrados
filtroBarras = (df['Country'] == pais) &(df['Year']==año)
df_filtrado = df.loc[filtroBarras] 
df_filtrado = df_filtrado.loc[:,['Country','Year','Life_expectancy']]    


st.title("Esperanza de Vida  Por País y Año" )

st.bar_chart(df_filtrado.set_index('Life_expectancy'))


st.title("Esperanza de Vida por Muerte de Infantes" )

filtroBarras2 = (df['Infant_deaths']==Muerte_de_Infantes)
df_filtrado2 = df.loc[filtroBarras2] 
df_filtrado2 = df_filtrado2.loc[:,['Infant_deaths','Country','Life_expectancy']]    

st.bar_chart(df_filtrado2.set_index('Life_expectancy'))


st.title("Esperanza de Vida por PBI" )

filtroBarras4 = (df['GDP_per_capita']==pib)
df_filtrado4 = df.loc[filtroBarras4] 
df_filtrado4 = df_filtrado4.loc[:,['GDP_per_capita','Country','Life_expectancy']]    

st.bar_chart(df_filtrado4.set_index('Life_expectancy'))


filtroBarras3 = (df['Region'] == region) &(df['Year']==año)
df_filtrado3 = df.loc[filtroBarras3] 
df_filtrado3 = df_filtrado3.loc[:,['Region','Year','Country','Life_expectancy']]    


st.title("Esperanza de Vida  Por Región y Año" )

st.bar_chart(df_filtrado3.set_index('Life_expectancy'))




filtroBarras5 = (df['Adult_mortality'] == Mortalidad_en_Adultos)
df_filtrado5 = df.loc[filtroBarras5] 
df_filtrado5 = df_filtrado5.loc[:,['Adult_mortality','Country','Life_expectancy']]    


st.title("Esperanza de Vida Por Mortalidad en Adultos" )

st.bar_chart(df_filtrado5.set_index('Life_expectancy'))
