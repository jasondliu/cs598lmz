import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches
from matplotlib.widgets import Button
from matplotlib.widgets import Slider
from matplotlib.widgets import RadioButtons

from scipy.integrate import odeint

from math import *

from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)

# Global variables

# Simulation parameters
dt = 0.01
t_max = 10

# Robot parameters
m = 1.0
l = 1.0
I = 1.0
g = 9.81

# Controller parameters
Kp = 10.0
Kd = 1.0

# Initial conditions
theta_0 = 0.0
theta_dot_0 = 0
