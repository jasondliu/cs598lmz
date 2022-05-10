import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from scipy.integrate import odeint
from scipy.optimize import minimize
from scipy.optimize import curve_fit

from scipy.stats import norm
from scipy.stats import multivariate_normal

from scipy.special import factorial
from scipy.special import binom

import time

import pandas as pd

from IPython.display import clear_output

import os

import warnings
warnings.filterwarnings('ignore')

import random

import copy

import math

import pickle

import seaborn as sns

import scipy.stats as stats

from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score

from sklearn.model_
