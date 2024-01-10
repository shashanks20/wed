from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
import matplotlib.pyplot as plt
import pandas as pd
iris = load_iris()
x = iris.data
y = iris.target
md1 = KMeans(n_clusters=3)
kmean = md1.fit_predict(x)
md2 = GaussianMixture(n_components=3)
gauss = md2.fit_predict(x)
plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
plt.scatter(x[:,0],x[:,1],c=kmean,cmap='viridis',edgecolors='k')
plt.title("KMeans")

plt.subplot(1,2,2)
plt.scatter(x[:,0],x[:,1],c=gauss,cmap='viridis',edgecolors='k')
plt.title("EM")

plt.show()

