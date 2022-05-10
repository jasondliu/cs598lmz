import threading
threading.stack_size(2**27)
import sys
import math
import os
import random
import time

import numpy as np
import scipy as sp
import pandas as pd

from sklearn import tree
from sklearn import ensemble
from sklearn import model_selection
from sklearn import linear_model
from sklearn import preprocessing
from sklearn import svm
from sklearn import neighbors
from sklearn import metrics

from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import AdaBoostClassifier

from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV

from sklearn.tree import DecisionTreeClassifier

# Suppress warnings
import warnings
warnings.filterwarnings("ignore")

# Set random seed
np.random.seed(0)

# Function to calculate accuracy
def calculate_accuracy(actual, predicted):
    count = 0
    for i in range(len(
