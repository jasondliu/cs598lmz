import gc, weakref
import contextlib
import os
import sys
import ctypes
import atexit

import numpy as np
import numpy.ctypeslib as npct

_curdir = os.path.abspath(os.path.dirname(__file__))
_libdir = os.path.join(_curdir, 'lib')

#------------------------------------------------------------------------
# Setup ctypes
#------------------------------------------------------------------------

if sys.platform == 'win32':
    _libext = '.dll'
else:
    _libext = '.so'

_libpath = os.path.join(_libdir, 'interp' + _libext)
_lib = npct.load_library('interp', _libpath)

_lib.interp_linear_2d_init.restype = ctypes.c_void_p
_lib.interp_linear_2d_init.argtypes = [npct.ndpointer(dtype=np.float32, ndim=2),
                                       ctypes.c_intp, ctypes.c_intp]

_lib.
