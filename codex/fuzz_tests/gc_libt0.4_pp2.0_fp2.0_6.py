import gc, weakref
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

from sklearn.preprocessing import PolynomialFeatures

from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.linear_model import ElasticNet

from sklearn.model_selection import GridSearchCV

%matplotlib inline

pd.options.display.max_columns = None
 
# load data
df = pd.read_csv('data/train.csv')
df.head()

# drop id column
df.drop(['Id'], axis=1, inplace=True)

# check for missing values
df.isnull().sum()

# check for duplicates
df[df.duplicated()]

# check for outliers

