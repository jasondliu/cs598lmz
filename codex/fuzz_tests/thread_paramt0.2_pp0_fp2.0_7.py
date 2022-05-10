import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from scipy.integrate import odeint
from scipy.optimize import minimize

from scipy.interpolate import interp1d

from scipy.signal import find_peaks

from scipy.stats import linregress

from scipy.special import erf

from scipy.signal import savgol_filter

from scipy.optimize import curve_fit

from scipy.signal import find_peaks

from scipy.signal import find_peaks_cwt

from scipy.signal import peak_widths

from scipy.signal import argrelextrema

from scipy.signal import argrelmax

from scipy.signal import argrelmin

from scipy.signal import argrelextrema

from scipy
