import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# Generate data
X, y = make_blobs(n_samples=500, centers=5, random_state=0)

# Plot data
plt.scatter(X[:, 0], X[:, 1], c='k')
plt.show()

# Initialize KMeans
kmeans = KMeans(n_clusters=5)

# Fit KMeans
kmeans.fit(X)

# Predict clusters
y_pred = kmeans.predict(X)

# Plot clusters
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.show()

# Print inertia
print(kmeans.inertia_)

# Initialize KMeans
