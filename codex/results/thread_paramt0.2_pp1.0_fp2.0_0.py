import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle

from scipy.integrate import odeint
from scipy.optimize import fsolve

from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
from IPython.display import display

from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import cnames
from matplotlib import animation

from scipy.integrate import odeint
from numpy import linspace

from matplotlib import animation, rc
from IPython.display import HTML

from scipy.integrate import odeint
from numpy import linspace

from matplotlib import animation, rc
from IPython.display import HTML

from scipy.integrate import odeint
from numpy import
