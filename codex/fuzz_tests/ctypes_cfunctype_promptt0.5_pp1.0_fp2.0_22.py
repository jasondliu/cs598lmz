import ctypes
# Test ctypes.CFUNCTYPE

import ctypes
import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# attach a CFUNCTYPE(None) to a prototype
def func(*args):
    pass

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)
qsort = lib.my_qsort
qsort.argtypes = (ctypes.c_void_p, ctypes.c_int, ctypes.c_int, CMPFUNC)
qsort.restype = None

# test default argument handling
qsort(None, 0, 0, func)

# test passing a CFUNCTYPE instance
qsort(None, 0, 0, CMPFUNC(func))

# test passing a function which is not a CFUNCTYPE instance
try:
    qsort(None, 0, 0, func)
except TypeError:
    pass
else:
    raise RuntimeError("should have raised TypeError")
