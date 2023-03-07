import streamlit as st
import numpy as np
import pandas as pd

st.header("My first Project App")
st.write(pd.DataFrame({
    'Intplan': ['TV', 'Radio', 'Newspaper', 'Sales'],
    'Churn Status': [0, 0, 0, 1]
}))
