import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches
from matplotlib.collections import PatchCollection

from scipy.integrate import odeint
from scipy.optimize import minimize

from scipy.interpolate import interp1d

from scipy.integrate import solve_ivp

from scipy.optimize import curve_fit

from scipy.interpolate import interp1d

from scipy.optimize import fsolve

from scipy.optimize import root

from scipy.optimize import brentq

from scipy.optimize import newton

from scipy.optimize import bisect

from scipy.optimize import fixed_point

from scipy.optimize import broyden1

from scipy.optimize import broyden2

from scipy.optimize import anderson


