import ctypes
ctypes.windll.user32.SetProcessDPIAware()

#%%

#%%
import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#%%
import tensorflow as tf

#%%
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

#%%
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.callbacks import ModelCheckpoint, TensorBoard

#%%
# Split the data into 70% training and 30% testing
train_data, test_data, train_labels, test_labels = train_test_split(features,
                                                                    labels,
                                                                    test_size=0.3,
                                                                    random_state=42)

#%%
# Standardize the training data
scaler = StandardScaler()
scaler.fit(train_data)

#%%

