import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split

from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD

from keras.utils import to_categorical

from keras.callbacks import EarlyStopping

from keras.models import load_model

#%%

X, y = make_moons(n_samples=1000, noise=0.1, random_state=0)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#%%

model = Sequential()
model.add(Dense(4, input_shape=(2,), activation='tanh'))
