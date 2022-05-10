import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a function pointer argument

# prototype of the function in the dll
CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# the function in the dll
lib.set_callback.argtypes = (CALLBACKFUNC,)

# the function to pass to the dll
def callback(value):
    print('callback called with', value)
    return value + 1

# call the dll function
lib.set_callback(CALLBACKFUNC(callback))

# call the callback function
lib.call_callback(5)

# call a function with a function pointer argument

# prototype of the function in the dll
CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# the function in the dll
lib.set_callback.argtypes =
