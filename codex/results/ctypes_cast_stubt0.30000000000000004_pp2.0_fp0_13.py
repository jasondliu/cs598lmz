import ctypes
ctypes.cast(0, ctypes.py_object)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import re
import time
import datetime
import pickle
import gc

import lightgbm as lgb
from sklearn.model_selection import KFold
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import LabelEncoder

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.filterwarnings('ignore')

pd.set_option('display.max_columns', None)

# os.chdir('/home/tom/mywork/some_test') #修改工作目录
# print(os.getcwd()) #打印当前工作目录

data_path = '/home/tom/mywork/some_test/data/'
save_path = '/home/tom/mywork/some_test/feature/
