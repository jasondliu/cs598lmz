import ctypes
# Test ctypes.CFUNCTYPE
from ctypes import *

import _ctypes_test

lib = CDLL(_ctypes_test.__file__)

def check(restype, argtypes, *args):
    global lib
    func = CFUNCTYPE(restype, *argtypes)(("testfunc", lib), ((1, "a"), (2, "b"), (3, "c")))
    res = func(*args)
    print(func.restype, func.argtypes, args, "->", res)
    return res

