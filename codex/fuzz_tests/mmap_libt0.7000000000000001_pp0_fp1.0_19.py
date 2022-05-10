import mmap
from math import *
from sympy import *
from copy import copy

from ROOT import *
#from rootpy import *

from math import *
from array import array

from scipy.special import *
from scipy.stats import poisson, binom
from scipy.optimize import minimize, minimize_scalar, root

from multiprocessing import Pool

import os

from aux import *


def fit_leak(name, t, s, N, pars, bkg):
    """
    Fits background for a given time window
    
    Parameters
    ----------
    name : str
        name of workspace
    t : array 
        time
    s : array
        signal
    N : array
        signal after pre-selection
    pars : array
        fit parameters
    bkg : array
        background
    """

    ws = RooWorkspace(name)
    ws.importClassCode(RooClassFactory.makeClass('RooPolynomial'),True)
    ws.importClassCode(RooClassFactory.
