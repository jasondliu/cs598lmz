import types
types.ModuleType.__repr__ = lambda self: self.__name__

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

import statsmodels.api as sm

from scipy import stats

import warnings
warnings.filterwarnings('ignore')

%matplotlib inline
 
# read the data
df = pd.read_csv('../data/house_prices.csv')

# set the random seed
np.random.seed(0)

# print the first 5 rows of data
df.head()

# print the last 5 rows of data
df.tail()

# print
