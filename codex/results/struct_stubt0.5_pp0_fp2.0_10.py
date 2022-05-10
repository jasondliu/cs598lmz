from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')

import numpy as np

from ._cffi import ffi, lib
from . import errors
from . import _util


def _check(value, param_name):
    if value is None:
        return
    if not isinstance(value, (int, float)):
        raise TypeError('%s must be a number' % param_name)


def _check_bool(value, param_name):
    if value is None:
        return
    if not isinstance(value, bool):
        raise TypeError('%s must be a bool' % param_name)


class _CudaContext(object):
    """
    Singleton class for managing CUDA context.

    The class is a singleton and should not be instantiated.
    """
    _instance = None

    def __init__(self):
        """
        Initializes the CUDA context.

        The CUDA context is initialized only once, even if
        several instances of the class are created.
        """
        if _CudaContext._instance is None:

