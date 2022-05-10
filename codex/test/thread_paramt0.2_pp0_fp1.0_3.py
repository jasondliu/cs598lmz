import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button, RadioButtons
from matplotlib.patches import Circle
from matplotlib.collections import PatchCollection
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable
from matplotlib.colorbar import ColorbarBase

from scipy.integrate import odeint
from scipy.interpolate import interp1d
from scipy.optimize import curve_fit
from scipy.special import erf

from time import time

from sklearn.metrics import mean_squared_error

from tqdm import tqdm

import pandas as pd

from IPython.display import clear_output

import warnings
warnings.filterwarnings('ignore')

import os

import seaborn as sns

