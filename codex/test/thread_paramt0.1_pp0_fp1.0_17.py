import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm

from scipy.integrate import odeint
from scipy.interpolate import interp1d

from IPython.display import HTML

from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets

from matplotlib import animation, rc
from IPython.display import HTML

from scipy.integrate import odeint
from scipy.interpolate import interp1d

from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets

from matplotlib import animation, rc
from IPython.display import HTML

from scipy.integrate import odeint
