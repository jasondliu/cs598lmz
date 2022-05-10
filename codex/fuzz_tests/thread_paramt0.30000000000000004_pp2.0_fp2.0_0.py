import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\x1b[2J\x1b[H")).start()

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from scipy.integrate import odeint
from scipy.interpolate import interp1d
from scipy.optimize import fsolve
from scipy.optimize import minimize
from scipy.optimize import curve_fit
from scipy.optimize import root
from scipy.optimize import brentq
from scipy.optimize import broyden1
from scipy.optimize import newton_krylov
from scipy.optimize import anderson
from scipy.optimize import linear_sum_assignment
from scipy.linalg import solve
from scipy.linalg import solve_banded
from scipy.linalg import lsts
