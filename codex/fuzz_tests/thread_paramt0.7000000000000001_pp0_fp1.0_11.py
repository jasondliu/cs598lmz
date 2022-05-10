import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n'*50)).start()
from sklearn.datasets import make_blobs, make_moons
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import euclidean_distances
import numpy as np
import time
from IPython.display import clear_output

from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.preprocessing import StandardScaler
import numpy as np
from IPython.display import clear_output
from copy import deepcopy


class K_Means():
    def __init__(self, k=2, max_iter=300, random_state=123):
        self.k = k
        self.max_iter = max_iter
        self.random_state = random_state

    def initializ_centroids(self, X):
        np.random.RandomState(self.random_state)

