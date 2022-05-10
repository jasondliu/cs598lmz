import sys, threading
threading.Thread(target=lambda:sys.stdout.write('\x1b[1;32m' + '-' * 70 + '\x1b[0m\n')).start()

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split

from ml_utils import *

# Load data
data = pd.read_csv('./data/train.csv', index_col=0)
data = data.dropna(subset=['Response'])
X = data.drop('Response', axis=1)
y = data['Response']

# Split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Train models
model_rf = RandomForestClassifier(n_estimators=100, min_samples_leaf=
