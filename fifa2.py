import streamlit as st
import pandas as pd
import plotly.express as px

st.title("FIFA EXPLORATORY DATA")
st.text('''This is the data for players and 
                this can be more advanced ''')

st.markdown("### The Best Five Players")

fifa=pd.read_csv('fifa_eda.csv')

col1, col2 = st.columns(2)

with col1:
    st.dataframe(fifa.nlargest(5,'Value')[['Name', 'Value']])

with col2:
    fig = px.bar(fifa.nlargest(5,'Value'), x='Name', y='Value', color='Club')

    #fig = px.scatter(fifa.nlargest(5,'Value'), x='Name', y='Value', color='Club')
    st.plotly_chart(fig)
    
players_avg_values = fifa.groupby('Nationality').mean()['Value']
nationality = fifa.Nationality.unique().tolist()
country_choice = st.selectbox("Choose Country",nationality)
st.write(fifa[fifa.Nationality == country_choice]['Value'].mean())