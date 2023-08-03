import streamlit as st
import plotly.express as px
import pandas as pd

st.title("In Search for Happiness")
x_axis = st.selectbox(label='Select the data for X-axis', options=('GDP', 'Happiness', 'Generosity'))
y_axis = st.selectbox(label='Select the data for Y-axis', options=('GDP', 'Happiness', 'Generosity'))
st.subheader(f"{x_axis} and {y_axis}")

df = pd.read_csv('happy.csv')

match x_axis:
    case 'Happiness':
        x_array = df['happiness']
    case 'GDP':
        x_array = df['gdp']
    case 'Generosity':
        x_array = df['generosity']

match y_axis:
    case 'Happiness':
        y_array = df['happiness']
    case 'GDP':
        y_array = df['gdp']
    case 'Generosity':
        y_array = df['generosity']

figure = px.line(x=x_array, y=y_array, labels={'x': x_axis, 'y': y_axis})
st.plotly_chart(figure)


