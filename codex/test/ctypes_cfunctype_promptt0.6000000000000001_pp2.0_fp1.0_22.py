import ctypes
# Test ctypes.CFUNCTYPE

# This is the prototype of the callback function used below.
CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# This is the callback function
@CALLBACKFUNC
def callback(x, y):
    return x + y

# This is a C function that calls the callback.
