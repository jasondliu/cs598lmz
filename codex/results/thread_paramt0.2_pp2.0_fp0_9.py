import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider

import time
import math

from scipy.integrate import odeint

from matplotlib.patches import Circle

from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)

# define the system of ODEs
def system(y, t, params):
    # unpack the parameters
    m, k, g, l = params
    # unpack the state vector
    theta, omega = y
    # compute the derivatives
    dydt = [omega, -(g/l)*np.sin(theta)]
    return dydt

# define the initial conditions
theta0 = np.pi/2.0
omega0 =
