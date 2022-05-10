import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from scipy.integrate import odeint
from scipy.optimize import minimize

from IPython.display import HTML

from matplotlib import rc
rc('animation', html='html5')

%matplotlib inline
 
# Define the system of ODEs
def model(y, t, params):
    S, I, R = y
    beta, gamma = params
    dSdt = -beta * S * I
    dIdt = beta * S * I - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

# Define the initial conditions
S0 = 0.99
I0 = 0.01
R0 = 0.00
y0 = S0, I0, R0

# Define the time points to solve for
t = np.
