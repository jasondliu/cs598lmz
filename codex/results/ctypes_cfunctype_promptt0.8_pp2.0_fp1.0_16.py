import ctypes
# Test ctypes.CFUNCTYPE()

import ctypes
import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)
cfunc = lib.testfunc_callback
cfunc.restype = ctypes.c_int
cfunc.argtypes = (ctypes.c_int, ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int))

def myfunc(a):
    return a * 2

result = cfunc(5, myfunc)

if result != 10:
    print("Got:", result, "Expected: 10")

result = cfunc(5, (ctypes.c_int * 2)())

if result != 10:
    print("Got:", result, "Expected: 10")

# Test calling functions through an instance.  The instance
# itself has no function, it's derived from Structure.

class Test(ctypes.Structure):
    pass

cfunc.argtypes = (ctypes.c_int, Test, ctypes.c_int)
cfunc.restype =
