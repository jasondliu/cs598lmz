import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

from keras.models import Sequential
from keras.layers import Dense, Dropout

from keras.optimizers import Adam
from keras.callbacks import EarlyStopping

from keras.utils.np_utils import to_categorical

import warnings
warnings.filterwarnings('ignore')

