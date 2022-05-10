import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle

from scipy.integrate import odeint
from scipy.optimize import curve_fit
from scipy.interpolate import interp1d
from scipy.integrate import quad

from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets

from IPython.display import display
from IPython.display import clear_output

from datetime import datetime

import os
import copy
import errno
import warnings

#%matplotlib notebook
