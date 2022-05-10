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
import sys

module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from src.models.SEIR import SEIR
from src.models.SEIRD import SEIRD
from src.models.SEIR_with_age import SEIR_with_age
from src.models.SEIRD_with_age import SEIRD_with_age
