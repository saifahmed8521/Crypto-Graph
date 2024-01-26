
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pickle
from streamlit_lottie import st_lottie

st.title("Etherium")

st.image('outputE3.png')
       
if st.button('Predict'):
       #st.subheader(select_crypto)
       st.image('outputE1.png')

if st.button('Predict Next 30Days'):
     #  st.subheader(select_crypto)
       st.image('outputE2.png')


# import json 
# import streamlit as st 
# from streamlit_lottie import st_lottie 

# path = "etherium_ani.json"
# with open(path,"r") as file: 
# 	url = json.load(file) 

# st_lottie(url, 
# 	reverse=True, 
# 	height=400, 
# 	width=400, 
# 	speed=1, 
# 	loop=True, 
# 	quality='high', 
# 	key='Car'
# )
