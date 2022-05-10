import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# prototype a function
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# create the function
restype = ctypes.c_int
argtypes = (ctypes.c_int,)

func = prototype((restype, argtypes), lib._testfunc_i_i)

# call the function
res = func(1)
print(res)

# prototype a function
prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# create the function
restype = ctypes.c_int
argtypes = (ctypes.c_int, ctypes.c_int)

func = prototype((restype, argtypes), lib._testfunc_i_ii)

# call the function
res = func(1, 2)
print(res)

# prototype a function
prototype = ctypes.CFUN
