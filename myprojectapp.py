import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LinearRegression
st.write("""
# My First project App
st.header("My first Project App")

This app predicts the **Sales** type!
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    TV = st.sidebar.slider('TV', 0, 200, 10)
    Radio = st.sidebar.slider('Radio', 0, 100, 10)
    Newspaper = st.sidebar.slider('Newspaper', 0, 100, 10)
             data = {'TV': TV,
            'Radio': Radio,
            'Newspaper': Newspaper,
features = pd.DataFrame(data, index=[0])
return features
df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

df = pd.read_csv('Advertising.csv')
df = df.drop(['Unnamed:0'],axis=1)
X = df.drop(['Sales'],axis=1
Y = df.Sales          

clf = LinerRegression()
clf.fit(X, Y)

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

st.subheader('Class labels and their corresponding index number')
st.write(iris.target_names)

st.subheader('Prediction')
st.write(iris.target_names[prediction])
#st.write(prediction)

st.subheader('Prediction Probability')
st.write(prediction_proba)
