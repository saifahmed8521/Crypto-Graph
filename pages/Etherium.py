import streamlit as st
from PIL import Image
from streamlit_extras.dataframe_explorer import dataframe_explorer

st.title("Etherium")

outputE3 = Image.open('outputE3.png')
st.image(outputE3)
       
if st.button('Predict'):
       outputE1 = Image.open('outputE1.png')
       st.image(outputE1)

if st.button('Predict Next 30Days'):
       outputE2 = Image.open('outputE2.png')
       st.image(outputE2)


Bitcoin = pd.read_csv('Etherium.csv')
Bitcoin1 = dataframe_explorer(Bitcoin,case=False)
st.dataframe(Bitcoin1, use_container_width=True)
