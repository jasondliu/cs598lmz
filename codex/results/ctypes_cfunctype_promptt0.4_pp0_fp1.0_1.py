import ctypes
# Test ctypes.CFUNCTYPE

import ctypes
from ctypes import *

import _ctypes_test

lib = CDLL(_ctypes_test.__file__)

def check(restype, argtypes, *args):
    func = CFUNCTYPE(restype, *argtypes)(("testfunc", lib), ())
    res = func(*args)
    print(res)
    return res

check(c_int, (c_int, c_int), c_int(3), c_int(4))
check(c_int, (c_float, c_float), c_float(3.1), c_float(4.1))
check(c_int, (c_double, c_double), c_double(3.1), c_double(4.1))
check(c_int, (c_longdouble, c_longdouble), c_longdouble(3.1), c_longdouble(4.1))
check(c_int, (c_int, c_float), c_int(3), c_float(4.1))
check(c_
