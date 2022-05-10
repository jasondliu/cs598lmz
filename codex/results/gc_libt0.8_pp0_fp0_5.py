import gc, weakref
import functools

import scipy.special as sp
import scipy.signal as ss

import numpy as np
import numpy.fft as nf

import matplotlib.pyplot as plt

import mpl_set
import fft_set

import logging
log = logging.getLogger(__name__)

class Sf_class(object):
    def __init__(self, size=1e+7, fdom=1.e+3, tdom=1., dt=1.e-4):
        self.size = int(size)
        self.fdom = fdom
        self.tdom = tdom
        self.dt   = dt
        self.fmax = self.fdom/(1.+np.log10(self.tdom)/10.)
        self.xf   = np.linspace(-self.fmax, self.fmax, self.size//2+1) 
        self.xt   = np.linspace(0., self.tdom, self.size)

    def get
