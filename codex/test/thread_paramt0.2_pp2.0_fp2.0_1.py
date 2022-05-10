import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button, RadioButtons
from matplotlib.patches import Circle

from scipy.integrate import odeint
from scipy.optimize import fsolve

from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import cnames
from matplotlib import cm

from math import pi, sin, cos, sqrt, atan2, acos, asin

from time import time

import json

from numpy import linalg as LA

from IPython.display import HTML

from matplotlib import animation, rc
from IPython.display import HTML

from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import cnames
from matplotlib import cm
