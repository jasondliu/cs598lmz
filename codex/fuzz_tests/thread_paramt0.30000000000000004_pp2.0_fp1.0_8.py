import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import os
import time

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

from scipy.spatial.distance import cdist

def kmeans_display(X, label):
    K = np.amax(label) + 1
    X0 = X[label == 0, :]
    X1 = X[label == 1, :]
    X2 = X[label == 2, :]
    
    plt.plot(X0[:, 0], X0[:, 1], 'b^', markersize = 4, alpha = .8)
    plt.plot(X1[:, 0], X1[:, 1], 'go', markersize = 4, alpha = .8)
    plt.plot(X2[:, 0], X2[:, 1], 'rs', markersize = 4, alpha = .8)

    plt
