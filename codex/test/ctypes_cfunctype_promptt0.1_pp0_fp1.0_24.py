import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# a function pointer
f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lib._testfunc_p_p)

# a function pointer to a function pointer
fp = ctypes.POINTER(ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int))
