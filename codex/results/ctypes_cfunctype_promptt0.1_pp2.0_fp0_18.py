import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a callback argument

# prototype of the callback function
CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# the callback function
def callback(value):
    print("callback called with", value)
    return value + 1

# the function taking the callback
lib.call_callback.argtypes = (CALLBACKFUNC, ctypes.c_int)
lib.call_callback.restype = ctypes.c_int

# call the function
result = lib.call_callback(CALLBACKFUNC(callback), 42)
print("result", result)

# call a function with a callback argument, and pass a
# callback function created by ctypes

# the callback function
def callback(value):
    print("callback called with", value)
    return value + 1

# the function taking the callback
lib.call_callback.argtypes = (CALLBACK
