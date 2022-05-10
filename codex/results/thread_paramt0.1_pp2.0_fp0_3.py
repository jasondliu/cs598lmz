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

#------------------------------------------------------------------------------
# Parameters
#------------------------------------------------------------------------------

# Simulation
dt = 0.01
t_max = 10

# Pendulum
l = 1
g = 9.81

#------------------------------------------------------------------------------
# Functions
#------------------------------------------------------------------------------

def pendulum(y, t, l, g):
    theta, omega = y
    dydt = [omega, -g/l*np.sin(theta)]
    return dydt

#------------------------------------------------------------------------------
# Main
#------------------------------------------------------------------------------

# Initial conditions
y0 = [np.pi/2, 0]

# Time
