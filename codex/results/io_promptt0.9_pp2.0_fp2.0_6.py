import io
# Test io.RawIOBase so that stdin is captured
# from: http://stackoverflow.com/questions/7654375/unit-testing-python-input
def get_input(user_input):
  stdin = sys.stdin
  sys.stdin = io.StringIO(user_input)
  yield
  sys.stdin = stdin
import pandas as pd
import numpy as np
import scipy as sp
import sklearn
import sys
import math
from IPython.display import display
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing
import copy


#loads data and splits into training and test sets

def split(df):
    msk = np.random.rand(len(df)) < 0.8
    train = df[msk]
    test = df[~msk]
    return train, test

def format(df):
	formatted_df=df.copy()
	#intuition, defailt and intl_plan are yes/no and not yes/
