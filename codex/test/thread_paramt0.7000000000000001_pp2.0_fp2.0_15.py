import sys, threading
threading.Thread(target=lambda: sys.stdin.read(1)).start()

import cv2
import numpy as np
import argparse
import os.path
import time
import math
import matplotlib.pyplot as plt
import scipy.stats as ss
from scipy.optimize import curve_fit
from scipy.stats import poisson, binom
from scipy.special import factorial, comb, erf, expi
from mpl_toolkits.mplot3d import Axes3D
import warnings

#General definitions
c = 2.99792458*10**8 #m/s
x = np.array([])

#Define the calibration info
#Polynomial fit to the image vs. position
#x, y
def fitFunction(x, a, b, c, d):
    return a*x**3 + b*x**2 + c*x + d

#x, y
def fitFunction2(x, a, b, c):
    return a*x**2 + b*x + c

#x, y
