import streamlit as st
import numpy as np
import pandas as pd

st.header("My first Project App")
st.write(pd.DataFrame({
    'Intplan': ['TV', 'Radio', 'Newspaper', 'Sales'],
    'Churn Status': [0, 0, 0, 1]
}))

from sklearn.naive_bayes import GaussianNB # 1. choose model class
model = GaussianNB()                       # 2. instantiate model
model.fit(Xtrain, ytrain)                  # 3. fit model to data
y_model = model.predict(Xtest)             # 4. predict on new data

from sklearn.metrics import accuracy_score
accuracy_score(ytest, y_model)
from sklearn.metrics import classification_report

print(classification_report(ytest, y_model)) 
