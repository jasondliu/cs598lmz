import threading
threading.stack_size(67108864)

import queue
import glob
import dill as pickle
import numpy as np
import pandas as pd
from copy import deepcopy
from PIL import Image
from tqdm import tqdm
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, MinMaxScaler, OneHotEncoder
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, precision_score, recall_score, roc_curve, auc


import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot as plt


np.random.seed(0)

from model_parameters import *
from model_operations import *

from keras.preprocessing.image import random_rotation, random_shift, random_zoom, random_shear
from keras.optimizers import Adam
from keras.callbacks import EarlyStopping, ModelCheckpoint, ReduceLROnPlateau, History
from
