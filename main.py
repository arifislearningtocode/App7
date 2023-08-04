import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place:")
days = st.slider(min_value=1, max_value=5, label="Forecast Days",
                 help='Select the number of forecasted days')
option = st.selectbox(label='Select data to view', options=('Temperature', 'Sky'))
st.subheader(f"{option} for the next {days} days in {place}")
if place:
    filtered_data = get_data(place, days)

    if option == 'Temperature':
        temperatures = [dict['main']['temp'] for dict in filtered_data]
        dates = []
        figure = px.line(x=dates, y=temperatures, labels={'x': 'Date', 'y': 'Temperature (C)'})
        st.plotly_chart(figure)

    if option == 'Sky':
        images = {'Clear': 'images/clear.png', 'Clouds': 'images/clouds.png',
                  'Rain': 'images/rain.png', 'Snow': 'images/snow.png'}
        sky_conditions = [dict['weather'][0]['main'] for dict in filtered_data]
        image_paths = [images[condition] for condition in sky_conditions]
        st.image(image_paths, width=115)


