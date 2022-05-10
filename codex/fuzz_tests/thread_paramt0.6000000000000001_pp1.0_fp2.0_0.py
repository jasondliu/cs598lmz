import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

from matplotlib import pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.colors import ListedColormap

import numpy as np
from numpy import pi

from scipy import interpolate
from scipy.integrate import quad
from scipy.optimize import curve_fit
from scipy.optimize import minimize
from scipy.optimize import minimize_scalar
from scipy.optimize import least_squares
from scipy.optimize import root
from scipy.optimize import fsolve

from scipy.interpolate import interp1d

from scipy.signal import argrelextrema
from scipy.signal import find_peaks_cwt
from scipy.signal import find_peaks

from scipy.stats import norm
from scipy.stats import linregress

from scipy.fftpack import fft
from scipy
