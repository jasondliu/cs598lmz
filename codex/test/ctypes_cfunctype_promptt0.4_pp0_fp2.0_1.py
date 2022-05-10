import ctypes
# Test ctypes.CFUNCTYPE
# This is not a complete test, just a few basic cases.

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

def test(restype, argtypes, *args):
    func = ctypes.CFUNCTYPE(restype, *argtypes)(("testfunc", lib), ())
    res = func(*args)
    print(func, args, "->", res)
    return res

