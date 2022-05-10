import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# call the function
func = prototype(("test_func", lib))
res = func(2)
if res != 2:
    raise RuntimeError("wrong result")

# call the function with a different prototype
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
func = prototype(("test_func", lib))
res = func(2)
if res != 2:
    raise RuntimeError("wrong result")

# call the function with a different prototype
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
func = prototype(("test_func", lib))
res = func(2, 3)
if res != 5:
    raise RuntimeError("wrong result")

# call the function with a different prototype
prototype
