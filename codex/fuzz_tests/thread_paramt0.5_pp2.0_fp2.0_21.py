import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import fetch_mldata
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load data from https://www.openml.org/d/554
X, y = fetch_mldata('mnist_784', version=1, return_X_y=True)

# split data into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)

# Train the classifier
clf = MLPClassifier(hidden_layer_sizes=(50,), max_iter=10, alpha=1e-4,
                    solver='sgd', verbose=10, tol=1e-4, random_state=1,
                    learning_rate_init=.1)

cl
