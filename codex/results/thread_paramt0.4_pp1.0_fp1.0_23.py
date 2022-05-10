import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H'),daemon=True).start()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from scipy.integrate import odeint
import time

#%%

def f(y,t):
    return np.array([y[1],-y[0]])

def f2(y,t):
    return np.array([y[1],-y[0]-y[1]])

def f3(y,t):
    return np.array([y[1],-y[0]-y[1]+np.sin(t)])

def f4(y,t):
    return np.array([y[1],-y[0]-y[1]+np.sin(t)+np.cos(
