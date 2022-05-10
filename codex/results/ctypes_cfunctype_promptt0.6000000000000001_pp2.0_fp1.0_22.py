import ctypes
# Test ctypes.CFUNCTYPE

# This is the prototype of the callback function used below.
CALLBACKFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# This is the callback function
@CALLBACKFUNC
def callback(x, y):
    return x + y

# This is a C function that calls the callback.
lib = ctypes.CDLL(ctypes.util.find_library('c'))
lib.call_callback.argtypes = [CALLBACKFUNC, ctypes.c_int, ctypes.c_int]
lib.call_callback.restype = ctypes.c_int

# The following should print '5'.
print(lib.call_callback(callback, 2, 3))
</code>

