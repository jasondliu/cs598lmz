import threading
threading.stack_size(1024*1024)
# import time

# get_ipython().magic('matplotlib inline')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.decomposition import PCA

# Import the dataset
# df = pd.read_csv('/home/yogesh/python/datasets/dataset1/data.csv')
# df = pd.read_csv('/home/yogesh/python/datasets/dataset2/data.csv')
# df = pd.read_csv('/home/yogesh/python/datasets/dataset3/data.csv')
df = pd.read_csv('/home/yog
