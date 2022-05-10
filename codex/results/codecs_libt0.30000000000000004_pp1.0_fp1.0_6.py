import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

import os
import sys
import time
import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.externals import joblib

# Set the working directory
os.chdir('C:/Users/dell/Desktop/Python/Kaggle/Titanic')

# Load the data
train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

# Check the data
train.head()
test.head()

# Check the data types
train.dtypes

# Check the missing values
train.isnull().sum()
test.isnull().sum()

# Check the number of unique values
