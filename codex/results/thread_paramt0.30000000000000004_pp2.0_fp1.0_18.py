import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

import warnings
warnings.filterwarnings('ignore')

%matplotlib inline

sns.set_style('whitegrid')

# Importing the dataset

df = pd.read_csv('USA_Housing.csv')
df.head()

# Exploring the dataset

df.info()
df.describe()
df.columns

# Exploratory Data Analysis

sns.pairplot(df)

# Distribution of the target variable

sns.distplot(df['Price'])

# Heatmap to check for correlation

sns.heatmap(df.corr(), annot=True)

# Training a Linear Regression
