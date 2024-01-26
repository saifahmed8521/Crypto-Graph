import streamlit as st
from PIL import Image




st.title("Bitcoin")

img = Image.open('outputE1.png')
st.image(img)

# if st.button('Predict'):
#      #  st.subheader(select_crypto)
#        st.image('outputN.png')

# if st.button('Predict Next 30Days'):
#      #  st.subheader(select_crypto)
#        st.image('outputN1.png')
