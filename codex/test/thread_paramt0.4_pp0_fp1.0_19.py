import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches

from scipy.ndimage.filters import gaussian_filter

import time
import math

from pylab import *
from numpy import *

from mpl_toolkits.mplot3d import Axes3D

from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

import scipy.io as sio

import os

import scipy.ndimage as ndimage

import scipy.ndimage.filters as filters

from scipy.ndimage import gaussian_filter

from scipy.stats import norm

import shutil

#%matplotlib inline

#%matplotlib qt

#%matplotlib notebook

#%matplotlib auto

#%matplotlib
