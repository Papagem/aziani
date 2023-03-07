from sklearn import preprocessing
scaler = preprocessing.MinMaxScaler()

df = pd.read_csv('Advertising.csv')

scaled=scaler.fit_transform(df)
df_scaled = pd.DataFrame(scaled)
df_scaled.head()

df_scaled.to_csv('Advertising.csv',index=False)


import streamlit as st
import numpy as np
import pandas as pd

st.header("My first Project App")
st.write(pd.DataFrame({
    'Intplan': ['TV', 'Radio', 'Newspaper', 'Sales'],
    'Churn Status': [0, 0, 0, 1]
}))
