import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from scipy.integrate import odeint
from scipy.optimize import minimize

from sklearn.metrics import mean_squared_error

from IPython.display import HTML

import warnings
warnings.filterwarnings('ignore')

%matplotlib inline
 
# Define the SIR model differential equations.
def deriv(y, t, N, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

# Define the SIR model differential equations.
def deriv_with_vaccination(y, t, N, beta, gamma, vaccination_rate):
    S, I, R = y
    dSdt = -beta * S * I
