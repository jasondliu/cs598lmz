import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointer must have the same signature as the
# CFUNCTYPE function we pass.

# The prototype of the function is:
# int function(int (*callback)(int))

# The prototype of the callback is:
# int callback(int)

# The function returns the value returned by the callback.

# The callback is called twice, with the arguments 42 and 17.

# The function returns the sum of the two values returned by the
# callback.

CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(value):
    print("callback called with", value)
    return value + 1

CALLBACK = CALLBACKFUNC(callback)

# The function returns the sum of the two values returned by the
# callback.

res = lib.function(CALLBACK)
print(res)

