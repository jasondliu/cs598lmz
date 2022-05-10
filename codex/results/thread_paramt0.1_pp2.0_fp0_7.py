import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from scipy.integrate import odeint
from scipy.optimize import minimize

from sklearn.metrics import mean_squared_error

from IPython.display import HTML

import pandas as pd

import warnings
warnings.filterwarnings('ignore')

import os

import time

import multiprocessing as mp

from multiprocessing import Pool

import pickle

from scipy.optimize import minimize

from sklearn.metrics import mean_squared_error

from IPython.display import HTML

import pandas as pd

import warnings
warnings.filterwarnings('ignore')

import os

import time

import multiprocessing as mp

from multiprocessing import Pool

import pickle

from scipy.optimize import minimize


