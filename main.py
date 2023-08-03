import streamlit as st

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place:")
days = st.slider(min_value=1, max_value=5, label="Forecast Days",
                 help='Select the number of forecasted days')
option = st.selectbox(label='Select data to view', options=('Temperature', 'Sky'))
st.subheader(f"{option} for the next {days} days in {place}")

