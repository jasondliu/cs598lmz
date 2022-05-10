import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p)

from scipy.spatial import cKDTree
from math import pi,acos,sin,cos
from copy import copy,deepcopy
from itertools import combinations
from numpy import array,zeros,ones,dot,vstack,tile,arange,asarray,float64,int32,abs
from numpy import sqrt,diag,set_printoptions,angle,log10,angle
from numpy.linalg import norm,inv,det
from numpy.random import uniform,random
from numpy.fft import fft,ifft,fftfreq,fftshift
from numpy.random import uniform,random
from numpy.linalg import norm,inv,det
from numpy.fft import fft,ifft,fftfreq,fftshift
set_printoptions(precision=2,suppress=True)
from constants import *
from functions import *
from classes import *


# calculate the phonon DOS and the phonon band structure from the Hessian
def calc
