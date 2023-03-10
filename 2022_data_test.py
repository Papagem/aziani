# -*- coding: utf-8 -*-
"""2022 Data test.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11hFS3NY6OrmzopxA8A3U3447YgCDVv8L
"""

!pip install sweetviz

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# importing sweetviz library
import sweetviz as sv

df = pd.read_excel('/content/2022 Data test2.xlsx')

df.shape

df.info

df.describe

df.fillna(0)

df.replace(np.nan,0)

pivot = df.pivot_table(index ="Channel", 
                       values ="Premium(RM)", aggfunc =sum)
pivot

pivot = df.pivot_table(index ="Agent Name",
                       values ="Premium(RM)", aggfunc =sum)
pivot

pivot2 = pivot.round(decimals = 2)
pivot2

df2 = df1.fillna(0)
df2

df3 = df2.round(decimals = 2)
df3

"""#unsupervised"""

import matplotlib.pyplot as plt
import numpy as np
df_defect = pd.read_excel('/content/2022 Data test2.xlsx')

df_defect.shape

df_defect.info()

from sklearn.datasets import make_blobs
X, y_true = make_blobs(n_samples=300, centers=4,
                       cluster_std=0.60, random_state=0)
plt.scatter(X[:, 0], X[:, 1], s=50);

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=4)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)

plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')

centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.5);

from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Generating the sample data from make_blobs

X, Y = make_blobs()

no_of_clusters = [2, 3, 4, 5, 6]

for n_clusters in no_of_clusters:

	cluster = KMeans(n_clusters = n_clusters)
	cluster_labels = cluster.fit_predict(X)

	# The silhouette_score gives the
	# average value for all the samples.
	silhouette_avg = silhouette_score(X, cluster_labels)

	print("For no of clusters =", n_clusters,
		" The average silhouette_score is :", silhouette_avg)

from sklearn.metrics import silhouette_score
no_of_clusters = [2, 3, 4, 5, 6]
for n_clusters in no_of_clusters:

	cluster = KMeans(n_clusters = n_clusters)
	cluster_labels = cluster.fit_predict(X)

	# The silhouette_score gives the
	# average value for all the samples.
	silhouette_avg = silhouette_score(X, cluster_labels)

	print("For no of clusters =", n_clusters,
		" The average silhouette_score is :", silhouette_avg)

no_of_clusters = [2, 3, 4, 5, 6]
distortions = []
for k in no_of_clusters:
    kmeanModel = KMeans(n_clusters=k)
    kmeanModel.fit(X)
    distortions.append(kmeanModel.inertia_)

plt.figure(figsize=(10,6))
plt.plot(no_of_clusters, distortions, 'bx-')
plt.xlabel('k')
plt.ylabel('Distortion')
plt.title('The Elbow Method showing the optimal k')
plt.show()