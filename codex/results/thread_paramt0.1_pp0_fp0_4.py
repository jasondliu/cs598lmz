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
def ode_system(y, t, params):
    # unpack the parameters
    a, b, c, d = params
    
    # unpack the state vector
    x, y = y
    
    # compute state derivatives
    dx_dt = a*x - b*x*y
    dy_dt = c*x*y - d*y
    
    # return the state derivatives
    return [dx_dt, dy_dt]

# Define the initial conditions
x0 = 10
y0 = 5

# Define the time points
