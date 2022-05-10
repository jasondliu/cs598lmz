import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm

from scipy.integrate import odeint
from scipy.interpolate import interp1d

from IPython.display import HTML

import time

from IPython.display import clear_output

from scipy.optimize import minimize

import os

import warnings
warnings.filterwarnings('ignore')

import pandas as pd

import matplotlib.pyplot as plt

import matplotlib.animation as animation

from IPython.display import HTML

import matplotlib.animation as animation

from IPython.display import HTML

import matplotlib.animation as animation

from IPython.display import HTML

import matplotlib.animation as animation

