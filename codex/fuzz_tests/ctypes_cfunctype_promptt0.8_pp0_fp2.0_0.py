import ctypes
# Test ctypes.CFUNCTYPE
from ctypes import CFUNCTYPE, c_int32, c_int
from test import support
from test.support import os_helper
from test.support.script_helper import assert_python_ok, assert_python_failure

from test.ctypes_test import needs_sni, needs_symbol_visibility, requires_symbol_visibility
from test.ctypes_test.test_callbacks import C_callback, C_callback_char_p

import _ctypes_test

lib = CDLL(_ctypes_test.__file__)

# add a callback function.
CMPFUNC = CFUNCTYPE(c_int, c_int, c_int)
qsort = lib.my_qsort
qsort.argtypes = (c_void_p, c_int, c_int, CMPFUNC)

def py_cmp_func(a, b):
    return a - b

CallbackFunc = CMPFUNC(py_cmp_func)
py_cmp_func.restype = c_int32
