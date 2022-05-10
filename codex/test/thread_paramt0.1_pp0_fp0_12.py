import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# Create dataset
X, y = make_blobs(n_samples=300, centers=4, random_state=0, cluster_std=0.60)

# Reshape data to get a 2D array
X = X[:, ::-1]

# Plot the data
plt.scatter(X[:, 0], X[:, 1])

# Create KMeans object
kmeans = KMeans(n_clusters=4)

# Fit the data
kmeans.fit(X)

# Get the cluster centroids
centroids = kmeans.cluster_centers_

# Get the cluster labels
labels = kmeans.labels_

# Plot the cluster centroids
