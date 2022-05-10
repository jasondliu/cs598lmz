import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lib._testfunc_i_i)
res = f(42)
if res != 42:
    raise RuntimeError("CFUNCTYPE test failed")

f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)(lib._testfunc_i_ii)
res = f(42, 43)
if res != 42 + 43:
    raise RuntimeError("CFUNCTYPE test failed")

f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)(lib._testfunc_i_iii)
res = f(42, 43, 44)
if res != 42 + 43 + 44:
    raise RuntimeError("CFUNCTYPE test failed")

f = ctypes
