import ctypes
ctypes.cast(1, ctypes.py_object)

x = np.empty(5, dtype=np.uint)
x[:] = 1
print(x)
print(x.dtype)

import sklearn.preprocessing as preprocessing
import pandas as pd
df = pd.DataFrame({'w.t': [2, 1, 1], 'w': [1, 2, 3]})
print(df)
print(preprocessing.scale(df, axis=0))

random.seed(12345)
print(random.randint(1, 100))

import numpy as np
print(np.random.randint(1, 100, 5))

import datetime
print(datetime.datetime.today().year)

import tensorflow as tf
print(tf.__version__)

import argparse
parser = argparse.ArgumentParser()
# Add argument
# parser.add_argument("echo", help="echo the string you use here")
parser.add_argument("square", help="display a square of a given number",
                    type=int
