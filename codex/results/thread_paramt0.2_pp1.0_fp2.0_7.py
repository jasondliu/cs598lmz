import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

from scipy.integrate import odeint
from scipy.optimize import minimize

from IPython.display import HTML

from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)

# Define the model
def model(y, t, params):
    S, I, R = y
    beta, gamma = params
    dSdt = -beta * S * I
    dIdt = beta * S * I - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

# Define the loss function
def loss(params, y, t, yobs):
    ymodel = odeint(model, y0, t, args=(params,))

