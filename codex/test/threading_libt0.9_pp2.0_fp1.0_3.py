import threading
threading.stack_size(2**27)

import numpy as np
import sys
from numba import jit
import math
import cmath
#from scipy import signal
import cProfile

num_threads = 6

def rotate(angle):
    return np.array([[math.cos(angle), -math.sin(angle)],
                     [math.sin(angle),  math.cos(angle)]])

def perp(a):
    return np.array([-a[1],a[0]])

@jit
def transformer(N,Nf,Dj,C,J,alpha,kappa):

    #assume C on uniform grid
    UJ = np.zeros((N,N,J+1),dtype=np.complex_)+0j

    #pull xij,wij, and u
