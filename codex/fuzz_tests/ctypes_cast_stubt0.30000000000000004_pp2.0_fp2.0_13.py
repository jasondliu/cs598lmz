import ctypes
ctypes.cast(None, ctypes.py_object)

import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Load the data
data = np.loadtxt("data.txt", delimiter=",")

# Split the data into X and y
X = data[:, 0:2]
y = data[:, 2]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Scale the data
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

# Train the model
mlp = MLPClassifier(hidden_layer_sizes=(10,
