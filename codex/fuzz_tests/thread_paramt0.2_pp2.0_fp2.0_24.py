import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button, RadioButtons

import time

from scipy.integrate import odeint

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
from matplotlib.widgets import Slider, Button, RadioButtons

import time

# define model
def model(z,t):
    x = z[0]
    y = z[1]
    dxdt = (x-x**3/3-y)*t
    dydt = x/t
    dzdt = [dxdt,dydt]
    return dzdt

# define time points
t = np.linspace(0,10,100)

# initial conditions
z0 = [1,1]

# solve ODE

