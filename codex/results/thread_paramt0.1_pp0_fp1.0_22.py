import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches
from matplotlib.collections import PatchCollection
from matplotlib.widgets import Slider, Button, RadioButtons

from scipy.integrate import odeint
from scipy.interpolate import interp1d
from scipy.optimize import minimize

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

from IPython.display import HTML

import pandas as pd

import os
import time
import pickle

import warnings
warnings.filterwarnings('ignore')

import seaborn as sns
sns.set()

from IPython.display import display, clear_output

import ipywidgets as widgets
from ipywidgets import interact, interactive, fixed, interact_manual

from IPython.display import display, clear_output

import ipy
