import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider, Button, RadioButtons

from scipy.integrate import odeint
from scipy.optimize import fsolve

from math import pi, sin, cos, sqrt

# Constants
g = 9.81
m = 1
l = 1

# Initial conditions
theta0 = pi/2
theta_dot0 = 0

# Time
t0 = 0
tf = 10
dt = 0.01
t = np.arange(t0, tf, dt)

# Solve ODE
def pendulum(y, t, b, c):
    theta, theta_dot = y
    dydt = [theta_dot, -b*theta_dot - c*sin(theta)]
    return dydt

