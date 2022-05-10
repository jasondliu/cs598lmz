import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("/home/graham/workspace/ml/ml.db")

import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '../..')))

import numpy as np
import pprint
import time
import datetime
import math
import logging
import log

if __name__ == '__main__':
    import mlr
    from mlr.mldata import Mldata

DATA_PATH = "data"

def get_init_time():
    # return time in seconds
    return time.mktime((2014, 11, 1, 0, 0, 0, 0, 0, 0))

class Data(object):
    "Base data class"
    def __init__(self):
        super(Data, self).__init__()

    def get_feature_names(self):
        raise NotImplementedError()

    def get_data(self, features=None):
        raise NotImplementedError()

