import gc, weakref

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder

from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.layers import Embedding
from keras.layers import LSTM
from keras.layers import GRU
from keras import optimizers

import xgboost as xgb

from tqdm import tqdm

import warnings
warnings.filterwarnings("ignore")

%matplotlib inline

# load the data
train = pd.read_csv('../input/train.csv')
test = pd.read_csv('../input/test.csv')

# create a submission dataframe
submission = pd.DataFrame()
submission['ID'] = test['ID']

# save the target column for training
target
