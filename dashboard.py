import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt

st.title("Dashboard Interativo com Streamlit")

data = {     'Ano': [2018, 2019, 2020, 2021, 2022],     'Vendas': [100, 150, 200, 250, 300] } 
df = pd.DataFrame(data)

fig, ax = plt.subplots() 
ax.plot(df['Ano'], df['Vendas'], marker='o') 
ax.set_title('Vendas Anuais') 
ax.set_xlabel('Ano') 
ax.set_ylabel('Vendas') 
st.pyplot(fig)

ano_min, ano_max = st.slider('Selecione o intervalo de anos', min_value=2018, max_value=2022, value=(2018, 2022))  
df_filtered = df[(df['Ano'] >= ano_min) & (df['Ano'] <= ano_max)]    
fig, ax = plt.subplots()  
ax.plot(df_filtered['Ano'], 
        df_filtered['Vendas'], marker='o')  
ax.set_title('Vendas Anuais')  
ax.set_xlabel('Ano')  
ax.set_ylabel('Vendas')

st.dataframe(df_filtered)
vendas_min = st.slider('Selecione o valor mínimo de vendas',min_value=int(df['Vendas'].min()), max_value=int(df['Vendas'].max()), value=int(df['Vendas'].min())) 
df_filtered = df[(df['Ano'] >= ano_min) & (df['Ano'] <= ano_max) & (df['Vendas'] >= vendas_min)] 
fig, ax = plt.subplots() 
ax.plot(df_filtered['Ano'], 
        df_filtered['Vendas'], marker='o') 
ax.set_title('Vendas Anuais') 
ax.set_xlabel('Ano') 
ax.set_ylabel('Vendas') 
st.pyplot(fig) 
st.dataframe(df_filtered)

st.write(""" # Dashboard de Vendas Este dashboard interativo permite visualizar os dados de vendas anuais. Use os sliders abaixo para filtrar os dados conforme necessário. """)