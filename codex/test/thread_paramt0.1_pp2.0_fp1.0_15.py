import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from scipy.integrate import odeint
from scipy.optimize import minimize

from scipy.interpolate import interp1d

from scipy.stats import norm

from scipy.signal import find_peaks

from scipy.special import erf

import pandas as pd

import os

import time

import pickle

import multiprocessing as mp

import itertools

import warnings
warnings.filterwarnings("ignore")

from IPython.display import clear_output

import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 300

import seaborn as sns
sns.set()

import matplotlib.pyplot as plt

from matplotlib import rc
