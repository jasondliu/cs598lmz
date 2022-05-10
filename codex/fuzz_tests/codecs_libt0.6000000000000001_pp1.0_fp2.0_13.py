import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'utf8mb4' else None)

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

import sklearn
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier, BaggingClassifier
from sklearn.svm import SVC
from sklearn.cross_validation import KFold

from sklearn.metrics import roc_curve, auc

from sklearn.metrics import classification_report

%matplotlib inline

import warnings
warnings.filterwarnings('ignore')

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# Read in the data
df = pd.read_csv('data/train.csv')
# Look at the data
df.head()

# Check for null values
df.isnull().sum()

# Check data types
df.dtypes

# Convert
