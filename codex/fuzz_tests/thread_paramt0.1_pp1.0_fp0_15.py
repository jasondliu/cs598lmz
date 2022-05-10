import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from scipy.integrate import odeint
from scipy.optimize import minimize

from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)

#%%

# Define the model
def model(y,t,p):
    S, I, R = y
    beta, gamma = p
    dSdt = -beta*S*I
    dIdt = beta*S*I - gamma*I
    dRdt = gamma*I
    return [dSdt, dIdt, dRdt]

#%%

# Define the objective function
def objective(p,y,t):
    # Model prediction
    y_hat = odeint(model,y0,t,args=(p,))
    # Calculate
