import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

import numpy as np
from numpy.linalg import norm
from scipy.optimize import minimize
from scipy.stats import norm as ndist

from selection.distributions.discrete_family import discrete_family
from selection.distributions.discrete_family import discrete_family_estimation

class discrete_family_estimation(discrete_family):

    def __init__(self, W, p, D, weights, data,
                 tuning_parameter,
                 V, U,
                 compute_intervals = True,
                 first_step = None,
                 second_step = None,
                 alpha = 0.05,
                 compute_intervals_first_step = True,
                 compute_intervals_second_step = True,
                 alternative = 'two-sided',
                 initial_sigma = None,
                 sigma_estimation = 'sample',
                 sigma_fixed = None,
                 confidence_intervals = False,
                 null_pivot = None,
                 null_
