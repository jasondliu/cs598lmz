import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from scipy.integrate import odeint
from scipy.optimize import fsolve

from math import *

# Constants

# Mass of the pendulum
m = 1

# Length of the pendulum
l = 1

# Gravity
g = 9.81

# Damping coefficient
b = 0.1

# Initial angle
theta0 = 0.1

# Initial angular velocity
omega0 = 0

# Initial state
x0 = [theta0, omega0]

# Time interval
t = np.linspace(0, 10, 1000)

# Solve the ODE
sol = odeint(lambda x, t: [x[1], -b*x[1] - (g/l)*sin(x[0])], x0, t)

# Plot the solution
plt
