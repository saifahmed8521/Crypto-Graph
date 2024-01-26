import streamlit as st
from PIL import Image




st.title("Bitcoin")

st.header('Method 1')
st.write('Here we use the image URL as the input argument to st.image')
st.code("st.image('https://drive.google.com/file/d/1b-RnnTWsaW1viiYrqks4y5jgK7c3Z11A/view?usp=sharing')")
st.image('https://drive.google.com/file/d/1b-RnnTWsaW1viiYrqks4y5jgK7c3Z11A/view?usp=sharing')

st.image('https://drive.google.com/file/d/1b-RnnTWsaW1viiYrqks4y5jgK7c3Z11A/view?usp=sharing')

# if st.button('Predict'):
#      #  st.subheader(select_crypto)
#        st.image('outputN.png')

# if st.button('Predict Next 30Days'):
#      #  st.subheader(select_crypto)
#        st.image('outputN1.png')
