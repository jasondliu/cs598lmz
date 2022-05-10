import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("darkgrid")

from sklearn.metrics import roc_curve, auc

import keras
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.callbacks import EarlyStopping, ModelCheckpoint

from collections import Counter

import os
import time
import random

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

from IPython.display import display

np.random.seed(7)


# In[2]:


def timer(start_time=None):
    if not start_time:
        start_time = datetime.now()
        return start_time
    elif start_time:
        thour, temp_sec = divmod((datetime.now() - start_time).total_seconds(), 3600
