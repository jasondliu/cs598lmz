import gc, weakref
import numpy as np
import numpy.linalg as la
import numpy.random as rnd
import scipy.linalg as sla
import scipy.integrate as itg
import scipy.optimize as opt
import scipy.special as spc

# --------------------------------------------------------------------------- #

# Library imports
import pyradbas.utils as utl
import pyradbas.distributions as dist
import pyradbas.kernels as krn
import pyradbas.quadratures as quad
import pyradbas.weight_functions as wf
import pyradbas.splines as spl

# --------------------------------------------------------------------------- #

# Global variable assignments
_default_reg = 1e-3
_default_eps = 1e-8

# --------------------------------------------------------------------------- #

class RBF_RS:
    """
    Implements the RBF-RS (Radial Basis Function Response Surface)
    """
    def __init__(self, X, Y, n_phi=1, n_theta=1,
                 phi_type='
