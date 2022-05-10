import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# Create dataset
X, y = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Plot dataset
plt.scatter(X[:,0], X[:,1])
plt.show()

# Initialize KMeans
kmeans = KMeans(n_clusters=4)

# Fit KMeans
kmeans = kmeans.fit(X)

# Predict clusters
predictions = kmeans.predict(X)

# Plot clusters
plt.scatter(X[:,0], X[:,1], c=predictions, cmap='rainbow')
plt.show()

# Plot centroids
pl
