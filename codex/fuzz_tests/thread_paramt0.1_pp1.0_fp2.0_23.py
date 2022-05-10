import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from scipy.integrate import odeint
from scipy.optimize import minimize

import time

from IPython.display import clear_output

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline

from scipy.optimize import curve_fit

from scipy.integrate import solve_ivp

from scipy.interpolate import interp1d

from scipy.optimize import fsolve

from scipy.optimize import root

from scipy.optimize import broyden1

from scipy.optimize import newton_krylov

from scipy.optimize import anderson

from scipy.optimize import linear_sum_assignment


