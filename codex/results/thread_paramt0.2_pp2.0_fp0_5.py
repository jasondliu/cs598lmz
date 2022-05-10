import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches
from matplotlib.collections import PatchCollection
from matplotlib.widgets import Slider, Button, RadioButtons

from scipy.integrate import odeint
from scipy.interpolate import interp1d

from IPython.display import HTML

from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)

import time

import warnings
warnings.filterwarnings("ignore")

import os

import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 300

import matplotlib.cm as cm

import matplotlib.gridspec as gridspec

import matplotlib.ticker as ticker
