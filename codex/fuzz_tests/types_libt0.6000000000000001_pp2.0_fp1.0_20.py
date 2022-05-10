import types
types.ModuleType.__reduce_ex__ = lambda self, proto: (getattr, (self, '__dict__'))

import sys
import logging
import argparse
import os.path
import csv
import ast
import json
import time
import random
import numpy as np
import pandas as pd
import seaborn as sns
import tensorflow as tf
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.utils import shuffle
from sklearn.ensemble import RandomForestRegressor

# from matplotlib import pyplot as plt

# from tensorflow.keras import Input, Model
# from tensorflow.keras.layers import Dense, Dropout, Activation, concatenate, Reshape
# from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint, ReduceLROnPlateau
# from tensorflow.keras.
