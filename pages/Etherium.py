import streamlit as st
from PIL import Image

st.title("Etherium")

outputE3 = Image.open('outputE3.png')
st.image(outputE3)
       
if st.button('Predict'):
       outputE1 = Image.open('outputE1.png')
       st.image('outputE1.png')

if st.button('Predict Next 30Days'):
       outputE2 = Image.open('outputE2.png')
       st.image('outputE2.png')
