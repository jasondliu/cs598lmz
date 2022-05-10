import gc, weakref
from math import pi, log
from numpy import ones, zeros, array, asarray, linspace, arange, \
     empty, hstack, vstack, dot, eye, sqrt, exp, log, newaxis, \
     concatenate, transpose, ceil, floor, zeros_like, ones_like
from numpy.linalg import norm, solve, LinAlgError
from scipy.optimize import fmin_bfgs, fmin_cg
from scipy.linalg import cho_factor, cho_solve, eigh
