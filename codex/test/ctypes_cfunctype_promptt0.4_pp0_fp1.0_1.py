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

