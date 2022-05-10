import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a callback argument

# prototype of the function in the dll
CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# the function in the dll
FUNC = lib.callbackfunc
FUNC.argtypes = (CALLBACKFUNC, ctypes.c_int)
FUNC.restype = ctypes.c_int

# the callback function
def mycallback(i):
    print("mycallback", i)
    return i + 1

# call the function in the dll
print(FUNC(CALLBACKFUNC(mycallback), 1))

# call a function with a callback argument, the callback
# function returns a pointer to a function

# prototype of the function in the dll
CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# the function in the d
