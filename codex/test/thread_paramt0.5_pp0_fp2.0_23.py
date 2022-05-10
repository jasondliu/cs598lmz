import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE

import seaborn as sns

import keras

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.utils import np_utils
from keras import backend as K

from keras.datasets import mnist

from keras.models import load_model

import os

#%%
(X_train, y_train), (X_test, y_test) = mnist.load_data()

#%%
X_train.shape, y_train.shape

#%%
