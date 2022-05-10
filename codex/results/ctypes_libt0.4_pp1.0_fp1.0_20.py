import ctypes
ctypes.cdll.LoadLibrary("libgomp.so.1")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

from gplearn.genetic import SymbolicRegressor
from gplearn.functions import make_function

from scipy.stats import pearsonr

from sklearn.metrics import mean_squared_error

from sklearn.model_selection import cross_val_score

from sklearn.preprocessing import PolynomialFeatures

from sklearn.linear_model import Ridge

from sklearn.linear_model import Lasso

from sklearn.linear_model import ElasticNet

from sklearn.linear_model import LassoLars

from sklearn.linear_model import LassoLarsIC

from sklearn.linear_model import OrthogonalMatchingPursuit

from sklearn.
