import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

cfunc = lib.my_callback
cfunc.argtypes = (ctypes.c_int, ctypes.c_int)
cfunc.restype = ctypes.c_int

def func(a, b):
    global func.count
    func.count += 1
    return a + b
func.count = 0

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

cfunc.argtypes = (CMPFUNC, ctypes.c_int, ctypes.c_int)
cfunc.restype = ctypes.c_int

res = cfunc(func, 1, 2)

if res != 3:
    raise RuntimeError("callback function returned %d, expected 3" % res)
if func.count != 1:
    raise RuntimeError("callback function was called %d times, expected 1" % func.count)

c
