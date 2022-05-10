import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from scipy.integrate import odeint
from scipy.interpolate import interp1d

from scipy.optimize import minimize

from scipy.stats import norm

from scipy.integrate import quad

from scipy.special import erf

from scipy.optimize import curve_fit

from scipy.stats import poisson

from scipy.stats import binom

from scipy.stats import chi2

from scipy.stats import gamma

from scipy.stats import expon

from scipy.stats import uniform

from scipy.stats import norm

from scipy.stats import t

from scipy.stats import chi2

from scipy.stats import f

from scipy.stats import beta

from scipy.stats import cauchy


