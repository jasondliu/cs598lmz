import threading
threading.stack_size(2**26)
import time
import os
import math
import matplotlib.pyplot as plt
from numpy import *
import pandas as pd
import xgboost as xgb
from matplotlib import pyplot
from sklearn import metrics, preprocessing, cross_validation
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from  datetime import datetime

train_file = 'sales_train.csv'
test_file = 'test.csv'
df = pd.read_csv(train_file, parse_dates=['date'])
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df_test = pd.read_csv(test_file)

item_categories = pd.read_csv('item_categories.csv')
shops = pd.read_csv('shops.csv')
