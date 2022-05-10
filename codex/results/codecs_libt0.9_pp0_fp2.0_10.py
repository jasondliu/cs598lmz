import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)
#%% Import All Dependancies
import pandas as pd
import os
from sys import argv
import glob
import numpy as np
from sklearn.feature_selection import VarianceThreshold
from sklearn.externals import joblib
from sklearn import svm
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.metrics import fbeta_score, make_scorer
import csv
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import GridSearchCV
import os
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import KFold
from sklearn.model_selection import cross
