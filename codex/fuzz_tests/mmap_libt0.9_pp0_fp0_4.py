import mmap
from time import time
from itertools import count
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error
from xgboost import XGBRegressor
import numpy as np
import os


PATH_TO_TRAIN_DATA = r"C:\Users\Admin\Desktop\netology\11\test_task_comments\train.tsv"
PATH_TO_TEST_DATA = r"C:\Users\Admin\Desktop\netology\11\test_task_comments\test.tsv"
PATH_TO_ANSWER = r"C:\Users\Admin\Desktop\netology\11\test_task_comments\answer.tsv"
TRAIN_SIZE = 1100000
TEST_SIZE = 300000


class DataReader(object):
    """
    Настройки:
        * headers - список заголовк
