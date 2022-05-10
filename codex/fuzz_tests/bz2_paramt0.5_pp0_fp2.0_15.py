from bz2 import BZ2Decompressor
BZ2Decompressor()

# 3rd party
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score

# local
from utils import *

# global vars
dataset_path = './datasets/Social_Network_Ads.csv'

# load dataset
dataset = pd.read_csv(dataset_path)

# split dataset into features and labels
X = dataset.iloc[:, [2,3]].values
y = dataset.iloc[:, 4].values

# split dataset into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

#
