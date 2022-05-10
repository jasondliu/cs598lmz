import gc, weakref
import numpy as np
import numpy.ma as ma
import numpy.random as ra
import pylab as pl
import pylab.imshow as imshow
import scipy.integrate as integrate
import scipy.ndimage as ndimage
import scipy.optimize as optimize
import scipy.signal as signal
from pyem import mrc
from pyem import dm
from pyem import unify_data,convert
import classify
from classify import mlp,pca,nmf,gmm,kmeans,em
import gputools
from gputools import ocl as cla

def colwise_norm(a):
    return float(a.size)**(-1/2) * cla.dot(a,a)**0.5

def colwise_center(a):
    return (a - a.mean(0))

def _colwise_center(a):
    a = a - a.mean(0)[None,:]
    return a

def _corr(a,b):
    return cla.dot(
