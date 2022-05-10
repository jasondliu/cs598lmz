import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
# db = sqlite3.connect('/Users/yuhuang/Projects/Kaggle/Santander/data/santander_train.db')
# db.close()
import pandas as pd
import numpy as np
import os
import time
import gc
import pickle
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='/Users/yuhuang/Projects/Kaggle/Santander/log/santander_train.log',
                    filemode='w')

console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

############
