import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double)

from scipy.optimize import fsolve
from scipy.integrate import ode
from scipy.optimize import least_squares
from scipy.signal import argrelextrema
from scipy.optimize import minimize
from scipy import optimize
from scipy.interpolate import interp1d
from scipy.special import jv
import matplotlib.pyplot as plt
import numpy as np
#from math import*
def set_functions(u):
    u_ = u.copy()
    def f(u, t, s):
        return(3.0*u*u/(2.0*(s+1.0)))
    def g(u):
        return((u_*u_ + u*u)/(2.0*(u_+u)))
    return(f, g)

def f(u, t, x):
    return(3.0*u*u/(2.0*(x+1.0)))

def g(u,
