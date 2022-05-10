import types
types.SimpleNamespace

# numpy
import numpy as np

# matplotlib
import matplotlib.pyplot as plt

# sklearn
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# keras
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.utils import to_categorical

# custom
from util import get_data, train_model

# set parameters
np.random.seed(0)
num_epochs = 10

# load data
X, Y = get_data()

# split into train, test
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=0)

# create model
model = Sequential()
model.add(Dense(128, activation='relu', input_dim=X.shape[
