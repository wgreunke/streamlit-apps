"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
df = pd.DataFrame({
  'first column': [7, 2, 3, 4],
  'second column': [11, 20, 30, 40]
})

df
