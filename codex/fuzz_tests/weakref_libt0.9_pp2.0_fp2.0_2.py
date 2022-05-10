import weakref
import warnings

import numpy as np
from scipy.optimize import leastsq
from scipy.special import gammainc
from scipy.integrate import quad
import pymc as pm
import theano

from .utils import imshow, imshow_mod, partial
from .array_models import GaussianMixture, GammaMixture
from .modelling import ModelPrior
from .draw import BaseScheduler, PriorScheduler, Histogram, sampling_histogram
from .graph_utils import NetworkInfo, GraphUtils

err = 'Error: '

# Primary package functions

def model_selection(methods=('BIC', 'AIC'), max_models=20):
    """ This is the current implementation of model selection, which is performed 
    by adding price arrays while monitor the BIC/AIC score
    """
    steps=len(methods)
    weights = []
    info = []
    for method in methods:
        for n_models in range(1, max_models+1):
            N, p = n_models+1, n
