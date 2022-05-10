import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from scipy.integrate import odeint
from scipy.optimize import minimize

from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import cnames
from matplotlib import animation

from IPython.display import HTML

#%matplotlib inline

# Define the Lorenz system
def lorenz(state, t, sigma, rho, beta):
    x, y, z = state
    return sigma * (y - x), x * (rho - z) - y, x * y - beta * z

# Define the Lorenz system
def lorenz_deriv(state, t0, sigma, rho, beta):
    x, y, z = state
    return [sigma * (y - x), x * (rho - z) - y, x * y - beta * z]

#
