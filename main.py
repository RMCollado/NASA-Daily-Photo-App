import os
import streamlit as st
import requests
from datetime import date

API_KEY = os.getenv("NASA_API_KEY")
NASA_URL = "https://api.nasa.gov/planetary/apod"
today = date.today()

today = today.strftime("%Y-%m-%d")

parameters = {
    "api_key": API_KEY,
    "date": today,
}

response = requests.get(url=NASA_URL, params=parameters).json()


image = response['url']

st.title(response['title'])

img_response = requests.get(url=image).content
st.image(img_response)


st.write(response['explanation'])
