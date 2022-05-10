import threading
threading.stack_size(2**27)

import sys
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import normalize
from sklearn.decomposition import PCA
from sklearn.cluster import MiniBatchKMeans

import os
os.chdir('/Users/michael/Desktop/Python/Python_Projects/Python_Projects/')

# Load data
dataframe = pd.read_csv('Wholesale customers data.csv')
dataframe.drop(['Region', 'Channel'], axis = 1, inplace = True)
print(dataframe.head())

# Normalize data
dataframe_norm = normalize(dataframe)
dataframe_norm = pd.DataFrame(dataframe_norm, columns=dataframe.columns)
print(dataframe_norm.head())

# Reduce it to two components.
pca = PCA(n_components=2)
