import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button, RadioButtons

import time

from scipy.integrate import odeint
from scipy.interpolate import interp1d

from numpy import sin, cos, tan, pi

from IPython.display import HTML

from matplotlib import rc
rc('animation', html='html5')

from matplotlib.patches import Circle, Wedge, Polygon
from matplotlib.collections import PatchCollection

from matplotlib.widgets import Slider, Button, RadioButtons

import matplotlib.gridspec as gridspec

import matplotlib.patches as patches

from matplotlib.patches import Circle, Wedge, Polygon
from matplotlib.collections import PatchCollection

from matplotlib.widgets import Slider, Button, Radio
