import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[2J\x1b[H')).start()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from scipy.integrate import odeint
from scipy.integrate import solve_ivp

from scipy.optimize import minimize

from scipy.integrate import ode

from scipy.interpolate import interp1d

from scipy.optimize import curve_fit

from scipy.signal import find_peaks

from scipy.stats import linregress

from scipy.interpolate import UnivariateSpline

from scipy.interpolate import CubicSpline

from scipy.interpolate import interp1d

from scipy.interpolate import InterpolatedUnivariateSpline

from scipy.interpolate import splrep, splev

from scipy.interpolate import make_interp_spline,
