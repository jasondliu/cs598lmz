import ctypes
ctypes.cdll.LoadLibrary("/usr/local/lib/libgsl.so")
ctypes.cdll.LoadLibrary("/usr/local/lib/libgslcblas.so")
import numpy as np

from pygsl.multifit import *
from pygsl.errors import *

from pygsl._numobj import *
from pygsl._numobj import _numobj
from pygsl._numobj import _swig_double as c_double
from pygsl._numobj import _swig_int as c_int
from pygsl._numobj import _swig_long as c_long

from pygsl.errors import PygslMemoryError
from pygsl.errors import PygslError

from pygsl.vector import Vector
from pygsl.matrix import Matrix
from pygsl.permutation import Permutation

from pygsl.ieee_utils import *

class FdFunc(object):
    """
    -------------------------------------------------
    This class is used to hold a function and its
    derivate in
