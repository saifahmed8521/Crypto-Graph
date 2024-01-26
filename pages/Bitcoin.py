import streamlit as st
from PIL import Image




st.title("Bitcoin")

st.header('Method 4')
st.write('Here we use Image.open as input to st.image. Relative path is input to Image.open.')
st.code("""
img = Image.open('outputE1.png')
st.image(img)
""")
img = Image.open('outputE1.png')
st.image(img)

st.image('outputE1')

# if st.button('Predict'):
#      #  st.subheader(select_crypto)
#        st.image('outputN.png')

# if st.button('Predict Next 30Days'):
#      #  st.subheader(select_crypto)
#        st.image('outputN1.png')
