import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

restype = ctypes.c_int
argtypes = (ctypes.c_int, ctypes.c_int)

# call a function
func = lib.add
func.restype = restype
func.argtypes = argtypes

res = func(1, 2)
if res != 3:
    raise RuntimeError("%d != 3" % res)

# call a function pointer
func = ctypes.CFUNCTYPE(restype, argtypes)(lib.add)
res = func(1, 2)
if res != 3:
    raise RuntimeError("%d != 3" % res)

# call a function pointer
func = ctypes.CFUNCTYPE(restype, argtypes)(lib.add)
res = func(1, 2)
if res != 3:
    raise RuntimeError("%d != 3" % res)

# call a function pointer
func = ctypes.CFUNCTYPE(restype, argtypes
