import threading
threading.stack_size(2**27)

import sys
import re
import os
import time
from datetime import datetime
import numpy as np
from numpy import random
from numpy.linalg import norm

from scipy.optimize import minimize
from scipy.optimize import least_squares
from scipy.optimize import curve_fit

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.linear_model import ElasticNet
from sklearn.linear_model import SGDRegressor
from sklearn.linear_model import TheilSenRegressor
from sklearn.linear_model import HuberRegressor
from sklearn.linear_model import RANSACRegressor
from sklearn.linear_model import PassiveAggressiveReg
