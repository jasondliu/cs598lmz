import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
from sklearn.metrics import accuracy_score, precision_score, recall_score, roc_curve, auc, confusion_matrix
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split

%matplotlib inline
plt.style.use('ggplot')

# load data
data_train_x = pd.read_csv('data/train_x.csv')
data_train_y = pd.read_csv('data/train_y.csv')
data_test_x = pd.read_csv('data/test_x.csv')
data_test_y = pd.read_csv('data/test_y.csv')
data_train_x.head()

