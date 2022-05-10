import sys, threading
threading.Thread(target=lambda: sys.stdout.write("")).start()
from numba import jit
import numpy as np
from scipy.integrate import odeint
from scipy.interpolate import Rbf
from scipy.special import erf, erfinv
from scipy.optimize import minimize
from scipy.stats import norm
from scipy.signal import savgol_filter
import time
from datetime import datetime
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
from matplotlib import cm
from matplotlib import pyplot as plt
import pickle
import random as rng
import os
import multiprocessing as mp
import datetime as dt
import time
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
import seaborn as sns

###############################################################################################
# Interpolation and integration
###############################################################################################
# Create the interpolating function
def createrbfit(x,y,z,dop
