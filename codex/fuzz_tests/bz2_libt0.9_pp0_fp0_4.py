import bz2
bz2.BZ2File
import sys
print(sys.path)
print(sys.executable)
print(sys.version)

 
# pip module
help('modules')

# matplotlib
import matplotlib.pyplot as plt
# %matplotlib inline

# numpy
import numpy as np
import scipy as sp
import pandas as pd

# sklearn
import sklearn
import sklearn.linear_model
import sklearn.neighbors       # KNN classifier
import sklearn.tree            # DecisionTree classifier
import sklearn.svm             # SVM classifier
import sklearn.ensemble        # Adaboost, RandomForest
import sklearn.neural_network  # FullyConnectedNetwork, Autoencoder

# tensorflow
import tensorflow as tf
from tensorflow.keras import backend as K
from tensorflow.keras.losses import mse, mae

# keras
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import
