import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import time

from scipy.optimize import minimize

from mpl_toolkits.mplot3d import Axes3D

import math

from scipy.optimize import minimize

from matplotlib import cm

from matplotlib.ticker import LinearLocator, FormatStrFormatter

from matplotlib.colors import LogNorm

from matplotlib.ticker import LogFormatterMathtext

from matplotlib.ticker import LogFormatter

from matplotlib.ticker import LogLocator

from matplotlib.ticker import MultipleLocator

from matplotlib.ticker import ScalarFormatter

from matplotlib.ticker import FormatStrFormatter

from matplotlib.ticker import LogFormatterExponent

from matplotlib.ticker import LogFormatterSciNotation
