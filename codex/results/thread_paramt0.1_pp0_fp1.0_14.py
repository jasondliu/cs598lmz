import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from scipy.integrate import odeint
from scipy.integrate import solve_ivp

from scipy.optimize import minimize

from scipy.interpolate import interp1d

from scipy.stats import norm

from scipy.special import erf

from scipy.signal import find_peaks

from scipy.optimize import curve_fit

from scipy.optimize import least_squares

from scipy.optimize import leastsq

from scipy.optimize import root

from scipy.optimize import fsolve

from scipy.optimize import brentq

from scipy.optimize import brenth

from scipy.optimize import bisect

from scipy.optimize import newton


