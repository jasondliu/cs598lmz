import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from scipy.integrate import odeint
from scipy.optimize import minimize

from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import cnames
from matplotlib import animation

import time

#%%

def lorenz(x, t, sigma, beta, rho):
    """The Lorenz equations."""
    u1, u2, u3 = x
    du1dt = sigma * (u2 - u1)
    du2dt = u1 * (rho - u3) - u2
    du3dt = u1 * u2 - beta * u3
    return du1dt, du2dt, du3dt

#%%

def lorenz_deriv(x_y_z, t0, sigma=10., beta=8./
