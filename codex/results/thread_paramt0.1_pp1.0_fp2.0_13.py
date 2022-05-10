import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from scipy.integrate import odeint
from scipy.interpolate import interp1d

from IPython.display import HTML

from matplotlib import rc
rc('animation', html='html5')

%matplotlib inline
 
# Define the function which returns the derivatives
def derivatives(y, t, N, beta, gamma):
    S, E, I, R = y
    dSdt = -beta * S * I / N
    dEdt = beta * S * I / N - gamma * E
    dIdt = gamma * E - gamma * I
    dRdt = gamma * I
    return dSdt, dEdt, dIdt, dRdt

# Define the initial conditions
N = 1000
D = 4.0 # infections lasts four days
gamma = 1.0 / D
R_0 = 5.0
beta = R
