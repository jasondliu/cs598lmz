import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from scipy.integrate import odeint
from scipy.optimize import minimize

from scipy.stats import norm

from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C

from mpl_toolkits.mplot3d import Axes3D

from IPython.display import clear_output

import time

import warnings
warnings.filterwarnings('ignore')

%matplotlib notebook
 
def lorenz(x, t, sigma, rho, beta):
    """
    The Lorenz equations.
    """
    u1, u2, u3 = x
    du1dt = sigma * (u2 - u1)
    du2dt = u1 * (rho - u3)
