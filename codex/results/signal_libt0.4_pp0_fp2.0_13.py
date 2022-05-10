import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import os
import sys
import time
import gc

import numpy as np
import pandas as pd

from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import roc_auc_score

import lightgbm as lgb

import matplotlib.pyplot as plt
import seaborn as sns

from contextlib import contextmanager

import warnings
warnings.filterwarnings("ignore")

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import artgor_utils
from utils import train_utils

%matplotlib inline

@contextmanager
def timer(title):
    t0 = time.time()
    yield
    print("{} - done in {:.0f}s".format(title, time.time() - t0))
    
def get_importance(model, features):
    feature_importance
