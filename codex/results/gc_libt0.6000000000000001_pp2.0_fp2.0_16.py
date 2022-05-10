import gc, weakref, sys

import numpy as np

from . import _get_c_funcs
from . import _get_c_types
from . import _get_c_constants
from . import _get_np_types

from . import _get_c_funcs as _r_get_c_funcs
from . import _get_c_types as _r_get_c_types
from . import _get_c_constants as _r_get_c_constants

from . import _get_c_funcs as _u_get_c_funcs
from . import _get_c_types as _u_get_c_types
from . import _get_c_constants as _u_get_c_constants

import ctypes
import ctypes.util

_c_lib = ctypes.cdll.LoadLibrary(ctypes.util.find_library('c'))
_c_lib.memcpy.argtypes = (
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes
