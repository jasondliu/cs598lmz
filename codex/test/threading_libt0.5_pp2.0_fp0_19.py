import threading
threading.stack_size(2**27)

# Start the main code
import numpy as np
import pandas as pd
import pickle
import sys
import time
import xgboost

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('data/creditcard.csv')
df.head()

# Count the number of fraud and non-fraud cases
non_fraud = df['Class'].value_counts()[0]
fraud = df['Class'].value_counts()[1]

# Print the results
print('There are {} non-fraud cases and {} fraud cases.'.format(non_fraud, fraud))

# Create X and y variables
