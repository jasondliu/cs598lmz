import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button, RadioButtons
from matplotlib.patches import Rectangle

from scipy.integrate import odeint
from scipy.optimize import fsolve

from math import pi, cos, sin, sqrt, log

from time import time

from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)

# Constants
g = 9.81
rho = 1.225

# Parameters
m = 0.5
l = 0.5
I = m*l**2/12

# Initial conditions
theta0 = 0.1
theta_dot0 = 0

# Time
t_start = 0
t_end = 10
N = 1000
t = np.linspace(
