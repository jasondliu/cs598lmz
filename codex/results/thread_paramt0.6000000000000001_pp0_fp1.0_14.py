import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\x1b[2J\x1b[H")).start()

import numpy as np
import matplotlib.pyplot as plt

from tqdm import tqdm
from scipy.optimize import minimize
from scipy.optimize import least_squares
from scipy.optimize import curve_fit

from scipy.integrate import odeint
from scipy.integrate import solve_ivp
from scipy.integrate import quad

from scipy.interpolate import interp1d
from scipy.interpolate import UnivariateSpline
from scipy.interpolate import CubicSpline

from scipy.stats import norm
from scipy.stats import multivariate_normal
from scipy.stats import chi2
from scipy.stats import kstest
from scipy.stats import ks_2samp
from scipy.stats import anderson
from scipy.stats import anderson_ksamp
from scipy.stats import ch
