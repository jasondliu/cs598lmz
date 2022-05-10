import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# call a function with a callback argument

# the callback function
def callback(x):
    print('callback called with', x)
    return x

CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# the function taking a callback as argument
lib.set_callback.argtypes = (CALLBACKFUNC,)
lib.set_callback.restype = None

lib.call_callback.argtypes = ()
lib.call_callback.restype = ctypes.c_int

# set the callback
lib.set_callback(CALLBACKFUNC(callback))

# call the callback
result = lib.call_callback()
print('callback returned', result)

# call a function with a callback argument

# the callback function
def callback(x):
    print('callback called with', x)
    return x

CALLBACKFUNC = ctypes.CFUNCTY
