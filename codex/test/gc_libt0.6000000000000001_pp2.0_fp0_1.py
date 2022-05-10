import gc, weakref
from time import time

from numpy import (
    array, dot, zeros, empty,
    allclose, sqrt, linalg,
    ndarray, vstack, all,
    nan_to_num, asarray
)
from numpy.linalg import norm
from numpy.random import rand

