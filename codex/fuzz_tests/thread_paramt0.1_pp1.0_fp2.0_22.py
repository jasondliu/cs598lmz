import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from scipy.integrate import odeint
from scipy.interpolate import interp1d

from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)

# Parameters

# Time
t_start = 0.0
t_end = 10.0
delta_t = 0.01

t_plot = np.arange(t_start, t_end+delta_t, delta_t)

# Initial conditions
x_0 = 0.0
y_0 = 0.0

# Constants
g = 9.81
m = 1.0

# Functions
def f(y, t, params):
    theta, omega = y      # unpack current values of y
    g, L = params  # un
