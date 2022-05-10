import ctypes
# Test ctypes.CFUNCTYPE
from ctypes import *
from ctypes.test import need_symbol
from ctypes.util import find_library

from test import support

libm = cdll.msvcrt

# A function taking a function pointer as argument.
# This is used to test callbacks.
# The function has the same name as the corresponding C function,
# but with a leading underscore, to prevent name clashes
# with the C functions in the dll.

def _callbackfunc(result, func, args):
    func.restype = c_int
    func.argtypes = [c_int]
    res = func(args[0])
    result[0] = res

CMPFUNC = CFUNCTYPE(c_int, c_int)
callbackfunc = CFUNCTYPE(None, POINTER(c_int), CMPFUNC, POINTER(c_int))

_callbackfunc_ptr = callbackfunc(_callbackfunc)

need_symbol('_ctypes_testfunc')
libm.use_callback.argtypes = (callbackfunc, POINTER(
