# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 18:20:18 2020

@author: VishalSharma
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv("Mall_Customers.csv")
data.head()
x=data.iloc[:,[3,4]].values
from sklearn.cluster import KMeans
from sklearn.cluster import KMeans
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
    kmeans.fit(x)
    # inertia method returns wcss for that model
    wcss.append(kmeans.inertia_)
print(i)