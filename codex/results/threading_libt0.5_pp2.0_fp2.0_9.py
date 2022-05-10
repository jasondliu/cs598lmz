import threading
threading.stack_size(2**27)

import sys
import logging
import gzip
import datetime
import time
import os

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.model_selection import GridSearchCV, ParameterGrid
from sklearn.metrics import average_precision_score

import lightgbm as lgb

from utils import load_data, process_data, process_data_fm, run_lgb, target_encode
from utils import IMP_FILE, IMP_FILE_FM, IMP_FILE_BAG
from utils import ITERATION, BAGGING_ITERATION, BAGGING_NUM, BAGGING_SEED

import pickle

import warnings
warnings.filterwarnings('ignore')

def main():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    handler = logging.FileHandler('feature_selection_lgbm.log')
