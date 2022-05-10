import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches

from scipy.integrate import odeint
from scipy.interpolate import interp1d

from matplotlib import style
style.use('fivethirtyeight')

#%%

# Constants

# Mass of the rocket in kg
m = 1.0
# Mass of the fuel in kg
m_p = 0.5
# Max thrust in N
T_max = 10.0
# Max burn time in s
t_b_max = 10.0
# Drag coefficient
C_D = 0.2
# Cross sectional area of the rocket in m^2
A = 0.1
# Gravitational acceleration in m/s^2
g = 9.81
# Air density in kg/m^3
rho = 1.2

#%%

# Simulation parameters

# Time step
dt = 0.01
# End
