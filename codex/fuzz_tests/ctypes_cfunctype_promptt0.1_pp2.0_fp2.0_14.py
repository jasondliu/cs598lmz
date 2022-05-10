import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a callback argument

# prototype of the function in the dll
CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# the function in the dll
PF = lib.prototyped_func
PF.argtypes = (CALLBACKFUNC, ctypes.c_int)
PF.restype = ctypes.c_int

# the callback
def mycallback(a, b):
    print("mycallback", a, b)
    return a + b

# call the function in the dll
res = PF(mycallback, 3)
print(res)

# call a function with a callback argument, and pass None

# the function in the dll
PF = lib.prototyped_func
PF.argtypes = (CALLBACKFUNC, ctypes.c_int)
PF.restype = ctypes.c
