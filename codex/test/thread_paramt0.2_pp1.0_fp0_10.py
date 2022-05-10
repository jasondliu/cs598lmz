import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from scipy.integrate import odeint
from scipy.interpolate import interp1d
from scipy.optimize import minimize

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

from IPython.display import HTML

import time

from tqdm import tqdm

import warnings
warnings.filterwarnings('ignore')

# %matplotlib inline
# %config InlineBackend.figure_format = 'retina'

# %load_ext autoreload
# %autoreload 2

# %load_ext nb_black

# %matplotlib widget

import matplotlib as mpl

mpl.rcParams["figure.dpi"] = 300
mpl.rcParams["savefig.dpi"] = 300
