import types
types.ModuleType.__init__ = lambda self, name, *args, **kwargs: None

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, classification_report

from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import Adam

from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import GridSearchCV

from keras.models import load_model

import warnings
warnings.filterwarnings('ignore')

# Set working directory
os.chdir('/home/ec2-user/SageMaker/wsu-ml/module-5/')

# Read data
df = pd.read_csv('data/creditcard.csv')

# Split data into X and y
X
