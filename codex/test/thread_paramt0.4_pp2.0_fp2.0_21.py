import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import colors
from matplotlib.widgets import Slider, Button, RadioButtons

from scipy.integrate import odeint

from matplotlib.widgets import Slider, Button, RadioButtons

import matplotlib as mpl
mpl.rcParams['toolbar'] = 'None'

# Define the function which calculates the derivatives
def deriv(y, t, N, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

# Define the function which calculates the derivatives
def deriv2(y, t, N, beta, gamma, delta):
    S, I, R, D = y
