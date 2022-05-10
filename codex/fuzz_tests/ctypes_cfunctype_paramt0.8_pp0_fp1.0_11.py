import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

import numpy as np
import os

import platform
if platform.system() != "Windows":
    from numba import jit

from scipy.optimize import newton

from . import _helper
from . import _sputils
from . import _spfunc

__all__ = ["BilinearInterp", "RecursiveInterp", "Interpolation", "CubicSpline", "SplineInterp"]


class BilinearInterp:
    """
    Bilinear interpolation

    This class is designed to perform bilinear interpolation.

    Parameters
    ----------
    x : array_like
        A sequence of x-coordinates.
    y : array_like
        A sequence of y-coordinates.
    z : array_like
        A sequence of either 1D or 2D array-like that are to be
        interpolated.

    Examples
    --------
    >>> x = np.arange(4)
    >>> y = np.arange(3)
    >>> z
