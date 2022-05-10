import ctypes
ctypes.cast(None, ctypes.py_object)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from scipy.integrate import ode
from scipy.integrate import odeint
from scipy.integrate import solve_ivp
from scipy.optimize import root
from scipy.optimize import fsolve
from scipy.optimize import broyden1
from scipy.optimize import broyden2
from scipy.optimize import newton_krylov
from scipy.optimize import anderson
from scipy.optimize import brentq
from scipy.optimize import brenth
from scipy.optimize import ridder
from scipy.optimize import bisect

from scipy.optimize import minimize
from scipy.optimize import basinhopping
from scipy.optimize import differential_evolution

from scipy.optimize import NonlinearConstraint
from scipy.optimize import LinearConstraint
