import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a callback

# prototype of the callback function
CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# the callback function
def callback(a, b):
    print("callback", a, b)
    return a + b

# the function taking the callback
lib.call_function.argtypes = (CALLBACKFUNC, ctypes.c_int)
lib.call_function.restype = ctypes.c_int

# call the function
res = lib.call_function(CALLBACKFUNC(callback), 3)
print("result", res)

# call a function with a callback, and pass a tuple as argument

# prototype of the callback function
CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

#
