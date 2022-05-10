import threading
threading.stack_size(2**27)
import sys
import subprocess
import os
from subprocess import PIPE,Popen
import re
import time

import random
import json
import numpy as np
import pandas as pd
import datetime
from sklearn import *
from catboost import CatBoostClassifier
import lightgbm as lgb
from multiprocessing import *


def multi(func, args, workers):
    with ProcessPoolExecutor(max_workers=workers) as ex:
        res = ex.map(func, args)
    return list(res)

def run_func(func,x):
    return func(*x)

def run_func_s(func,x):
    return func(x)

def run_func_t(func,x):
    return func(**x)


def get_type_list(df, flag_col):
    target_col = df.columns[-1]
    dtype_dict = {}
