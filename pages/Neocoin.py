import streamlit as st

st.title("Neocoin")

outputN2 = Image.open('outputN2.png')
st.image(outputN2)

if st.button('Predict'):
      outputN = Image.open('outputN.png')
      st.image(outputN)

if st.button('Predict Next 30Days'):
     outputN1 = Image.open('outputN1.png')
     st.image(outputN1)
    
