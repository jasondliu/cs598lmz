import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider

from scipy.integrate import odeint

from mpl_toolkits.mplot3d import Axes3D

from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

from matplotlib.colors import LogNorm

from matplotlib.widgets import Button

import matplotlib.patches as patches

import matplotlib.gridspec as gridspec

import matplotlib.patches as mpatches

import matplotlib.lines as mlines

import matplotlib.cbook as cbook

import matplotlib.image as mpimg

import matplotlib.colors as colors

import matplotlib.colorbar as colorbar

import matplotlib.patheffects as path_effects

import
