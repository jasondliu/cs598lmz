import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from scipy.integrate import odeint
from scipy.optimize import minimize

from sklearn.metrics import mean_squared_error

from IPython.display import HTML

from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import cnames
from matplotlib import animation

from scipy.integrate import odeint
from scipy.optimize import minimize

from sklearn.metrics import mean_squared_error

from IPython.display import HTML

from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import cnames
from matplotlib import animation

from scipy.integrate import odeint
from scipy.optimize import minimize

from sklearn.metrics import mean_squ
