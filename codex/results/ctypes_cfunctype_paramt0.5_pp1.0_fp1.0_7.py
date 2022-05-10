import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)
from scipy.integrate import quad
from scipy.integrate import fixed_quad
from scipy.integrate import quadrature
from scipy.integrate import romberg
from scipy.integrate import romb
from scipy.integrate import simps
from scipy.integrate import trapz
from scipy.integrate import cumtrapz
from scipy.integrate import odeint
from scipy.integrate import ode
from scipy.integrate import solve_ivp
from scipy.integrate import RK45
from scipy.integrate import LSODA
from scipy.integrate import DOP853
from scipy.integrate import Radau
from scipy.integrate import BDF
from scipy.integrate import complex_ode
from scipy.integrate import complex_odeint
from scipy.integrate import odeint_with_events
from scipy.integrate import solve_bvp
from
