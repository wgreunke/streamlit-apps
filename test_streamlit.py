"""
"""


import streamlit as st
import pandas as pd
import numpy as np


# *******************  Server **********************
age="" #Set inital value for Age.

df = pd.DataFrame({
  'first column': [7, 2, 3, 4],
  'second column': [11, 20, 30, 40]
})


""" *****************UI Elements********************* 
"""

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["col1", "col2", "col3"])
chart_data['col4'] = np.random.choice(['A','B','C'], 20)

age = st.slider('How old are you?', 0, 130, 25)

st.scatter_chart(chart_data,x='col1',y='col2',color='col4',size='col3',)



df
