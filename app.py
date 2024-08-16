import streamlit as st
import streamlit as st
from geopy.geocoders import Nominatim
import requests

st.markdown('''
# New York Taxifare predictor

##  Select an address and destination :taxi:
''')
geolocator = Nominatim(user_agent="geoapiExercises")

with st.form("Fill this form"):
    pickup_address = st.text_input("Enter pickup address :")
    dropoff_address = st.text_input("Enter dropoff address :")

    d = st.date_input("When will you travel ?")
    t = st.time_input("Set departure time :")

    if pickup_address:
        pickup = geolocator.geocode(pickup_address)
        if pickup:
            pickup_latitude = pickup.latitude
            pickup_longitude = pickup.longitude
        else:
            st.write("No address!")

    if dropoff_address:
        dropoff = geolocator.geocode(dropoff_address)
        if dropoff:
            dropoff_latitude = dropoff.latitude
            dropoff_longitude = dropoff.longitude
        else:
            st.write("No address!")

    passenger_count = st.select_slider(
        "Select a number of passengers",
        options=[1,2,3,4,5,7,8])
    submit_button = st.form_submit_button(label="Submit")




dt = f'{d} {t}'
params = {'pickup_datetime': dt, 'pickup_longitude' : pickup_longitude,
              'pickup_latitude' : pickup_latitude, 'dropoff_longitude' : dropoff_longitude ,
             'dropoff_latitude' : dropoff_latitude, 'passenger_count' : passenger_count }

url = 'https://taxifare.lewagon.ai/predict'


r = requests.get(url, params)
pred_fare = r.json()
st.write("The fare for this trip is",f"$ {round(pred_fare['fare'], 2)}")


st.markdown('''

###  Thanks ! Give us a feedback :)

''')
sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")
