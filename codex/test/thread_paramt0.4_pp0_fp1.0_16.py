import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import Adam

# Loading dataset
dataset = pd.read_csv('Churn_Modelling.csv')

# Checking the first 5 rows of the dataset
# print(dataset.head())

# Checking the shape of the dataset
# print(dataset.shape)

# Checking the last 5 rows of the dataset
# print(dataset.tail())

# Checking the info of the dataset
# print(dataset.info())

# Checking the statistical information of the dataset
# print(dataset.describe())

#
