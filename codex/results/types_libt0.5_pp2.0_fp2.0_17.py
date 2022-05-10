import types
types.ModuleType.__call__ = types.ModuleType

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

import pycuda.driver as cuda
import pycuda.autoinit
import pycuda.gpuarray as gpuarray
import pycuda.driver as drv
from pycuda.compiler import SourceModule
import pycuda.cumath as cumath

import cudakernels

from matplotlib import rcParams
rcParams['font.family'] = 'serif'
rcParams['font.size'] = 14
rcParams['text.usetex'] = True

import time

def main():
    """
    """

    # Parameters
    nx = 4096
    ny = 4096
    hx = 1.0/(nx-1)
    hy = 1.0/(ny-1)
    sigma = 0.5
    nu = 0.1
    dt = sigma*hx*hy/nu

    # Initial conditions
    u = np.zeros
