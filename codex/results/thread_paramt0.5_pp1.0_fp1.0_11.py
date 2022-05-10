import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

from scipy.integrate import odeint
from scipy.optimize import minimize
from scipy.interpolate import interp1d
from scipy.integrate import quad

import time

from matplotlib import animation, rc
from IPython.display import HTML

from IPython.core.display import display, HTML
display(HTML("<style>.container { width:90% !important; }</style>"))

# # %matplotlib notebook

# %matplotlib inline

# # %matplotlib tk

# plt.style.use('ggplot')

# import matplotlib as mpl

# mpl.rcParams['lines.linewidth'] = 2
# mpl.rcParams['lines.color'] = 'r
