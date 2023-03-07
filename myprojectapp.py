import streamlit as st
import numpy as np
import pandas as pd

st.header("My first Project App")
st.write(pd.DataFrame({
    'Intplan': ['TV', 'Radio', 'Newspaper', 'Sales'],
    'Churn Status': [0, 0, 0, 1]
}))

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 5)
knn

knn.fit(Xtrain, ytrain)

knn.score(Xtest, ytest)

from sklearn.metrics import accuracy_score
