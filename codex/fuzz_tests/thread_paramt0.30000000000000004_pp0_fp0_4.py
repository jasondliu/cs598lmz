import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from numpy import pi, sin, cos, tan, exp, log, sqrt
from numpy.random import rand, randn

from time import time, sleep

from IPython.display import clear_output

from scipy.integrate import odeint

from scipy.optimize import minimize

from scipy.interpolate import interp1d

from sklearn.linear_model import LinearRegression

import pandas as pd

from scipy.linalg import solve

from scipy.integrate import solve_ivp

from scipy.optimize import root

from scipy.interpolate import interp1d

from scipy.optimize import minimize

from scipy.linalg import solve

from scipy.integrate import solve_ivp

from sc
