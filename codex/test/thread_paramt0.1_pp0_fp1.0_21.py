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

import time

import os

import multiprocessing as mp

import pickle

import random

import math

import copy

import itertools

import scipy.stats as stats

import scipy.special as special

import scipy.integrate as integrate

import scipy.optimize as optimize

import scipy.interpolate as interpolate

import scipy.spatial as spatial

import scipy.linalg as linalg

import scipy.cluster as cluster

