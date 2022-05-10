import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button, RadioButtons

import time
import math

from scipy.integrate import odeint
from scipy.optimize import fsolve

from mpl_toolkits.mplot3d import Axes3D

from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

from matplotlib.colors import LogNorm

from matplotlib.backends.backend_pdf import PdfPages

from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator

from matplotlib.widgets import Slider, Button, RadioButtons

import matplotlib.gridspec as gridspec

import matplotlib.patches as patches

import matplotlib.patches as mpatches

from matplotlib.widgets import Sl
