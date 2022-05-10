import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from mpl_toolkits.mplot3d import Axes3D

from IPython.display import clear_output

from numpy import pi
from numpy import sin
from numpy import cos
from numpy import sqrt

from numpy.linalg import norm
from numpy.linalg import inv

from scipy.integrate import odeint
from scipy.integrate import solve_ivp

from scipy.optimize import minimize
from scipy.optimize import fsolve

import time

from IPython.display import clear_output

from scipy.optimize import root

from scipy.optimize import fsolve

import time

import matplotlib.pyplot as plt

from scipy.optimize import root

from scipy.optimize import fsolve

