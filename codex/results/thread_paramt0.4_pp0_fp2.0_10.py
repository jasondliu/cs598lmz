import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\n")).start()

import os
import time
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.utils import check_random_state

print('Fetch MNIST dataset...')
mnist = fetch_openml('mnist_784', version=1)
mnist.target = mnist.target.astype(np.int64)

print('Prepare train/test data...')
random_state = check_random_state(0)
permutation = random_state.permutation(mnist.data.shape[0])
X = mnist.data[permutation]
y = mnist.target[permutation]
X = X.reshape((X.shape[0], -1))

X_train, X_test, y_train, y_test = train_
