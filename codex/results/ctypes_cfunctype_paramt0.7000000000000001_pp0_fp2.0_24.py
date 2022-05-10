import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)

from math import pi
from math import atan, cos, sin
from copy import copy, deepcopy
from itertools import product
from functools import reduce

from numpy import matrix
from numpy import array
from numpy import linalg
from numpy import zeros
from numpy import ones
from numpy import identity
from numpy import mod
from numpy import cos, sin
from numpy import inf

from numpy.linalg import matrix_power
from numpy.linalg import norm
from numpy.linalg import eig
from numpy.linalg import inv
from numpy.linalg import det

from numpy.random import randn
from numpy.random import rand
from numpy.random import uniform
from numpy.random import randint
from numpy.random import permutation

from numpy.fft import fft
from numpy.fft import ifft
from numpy.fft import fft
