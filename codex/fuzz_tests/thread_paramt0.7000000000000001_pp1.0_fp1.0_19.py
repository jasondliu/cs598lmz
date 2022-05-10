import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\r\x1b[2J\x1b[H")).start()

from keras.models import Sequential
from keras.layers import Dense
from keras.callbacks import EarlyStopping
from keras.optimizers import Adam
from sklearn.model_selection import train_test_split
#from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import median_absolute_error
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from util import normalize
import time
from tqdm import tqdm
import os
import sys
from keras import backend as K
from keras.layers import Input, Conv3D, MaxPooling3D, UpSampling3D, BatchNormalization, Deconvolution3D, Activation, Cropping3D
from keras.models import Model
from keras.optimizers import Adadelta, Adam
