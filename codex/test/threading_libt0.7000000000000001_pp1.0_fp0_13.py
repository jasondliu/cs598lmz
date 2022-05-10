import threading
threading.stack_size(2**27)
import sys
import collections
sys.path.append('../../')
from datetime import datetime
from dateutil.relativedelta import relativedelta
from scipy import stats
import statsmodels.api as sm
import statsmodels.formula.api as smf
import pandas as pd
import numpy as np
from copy import copy
import itertools
from time import time, sleep
from IPython import display
from scipy.optimize import minimize
from random import shuffle
from sklearn import linear_model
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import KFold
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import RidgeCV
from sklearn.linear_model import LassoCV
from sklearn.metrics import mean_squared_error
import xgboost as xgb
