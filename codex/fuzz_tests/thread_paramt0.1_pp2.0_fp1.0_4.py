import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider, Button, RadioButtons

from scipy.integrate import odeint
from scipy.interpolate import interp1d
from scipy.optimize import curve_fit

from math import pi, sqrt, log, exp, log10, floor
from cmath import phase
from random import random

from time import time

from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)

#%%

def f(y, t, a, b, c, d):
    x, y = y
    return [a*x - b*x*y, -c*y + d*x*y]

def f_jac(y, t, a, b, c, d):

