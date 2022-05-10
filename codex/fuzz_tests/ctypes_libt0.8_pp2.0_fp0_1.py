import ctypes
ctypes.cdll.LoadLibrary("libgsl.so")
ctypes.cdll.LoadLibrary("libgslcblas.so")
import numpy as np
import scipy
from scipy.stats import norm
from scipy.optimize import minimize
import scipy.integrate as integrate
import os

def model(x,data,r=None,k=1.0):
    """
    This model is for fitting a Gaussian distribution with a simple
    exponential cut-off.
    
    x contains the parameters of the model:
    
    x[0] = Mu
    x[1] = Sigma
    x[2] = Tau
    x[3] = A
    
    data is a 2D numpy array containing the data for the model:
    
    data[:,0] = x values
    data[:,1] = y values
    """
    if r is None:
        y = x[3]*norm.pdf(data[:,0],x[0],x[1])*np.exp(-data[:,0]/x[2])
