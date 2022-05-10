import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

import sys
import os

#Change the working directory using the path to the directory that contains your data
os.chdir(r'C:\\')

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC

import seaborn as sns

#number of rows to show when using the methods head() and tail() in a DataFrame
pd.options.display.max_rows = 1000

#number of columns to show when using the method head() in a DataFrame
pd.options.display.max_columns = 20

%matplotlib inline

#Read the data from
