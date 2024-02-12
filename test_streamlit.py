"""
"""


import streamlit as st
import pandas as pd
df = pd.DataFrame({
  'first column': [7, 2, 3, 4],
  'second column': [11, 20, 30, 40]
})

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

df
