import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from scipy.integrate import odeint
from scipy.interpolate import interp1d

from matplotlib import style
style.use('fivethirtyeight')

#%%
# Define the function which calculates the derivatives
def derivatives(y, t, a, b, c, d):
    x, y = y
    dydt = [a*x - b*x*y, c*x*y - d*y]
    return dydt

#%%
# Define the initial conditions
x0 = 10
y0 = 5

# Define the time points for which we want to solve the ODE
t = np.linspace(0, 5, 100)

#%%
# Define the parameters
a = 1.0
b = 0.2
c = 0.1
d = 1.5

#%%
# Solve the ODE
y
