import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

from scipy.integrate import odeint
from scipy.optimize import minimize

from scipy.interpolate import interp1d

from scipy.integrate import solve_ivp

from scipy.optimize import curve_fit

from scipy.integrate import odeint

from scipy.integrate import simps

from scipy.integrate import quad

from scipy.integrate import nquad

from scipy.integrate import dblquad

from scipy.integrate import tplquad

from scipy.integrate import fixed_quad

from scipy.integrate import quadrature

from scipy.integrate import romberg

from scipy.integrate import newton_cotes

from scipy.integrate import trapz

