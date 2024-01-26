import streamlit as st
from PIL import Image

st.title("Bitcoin")

output5 = Image.open('output5.png')
st.image(output5)

if st.button('Predict'):
  output1 = Image.open('output1.png')
  st.image(output1)

if st.button('Predict Next 30Days'):
      output3 = Image.open('output3.png')
      st.image(output3)
