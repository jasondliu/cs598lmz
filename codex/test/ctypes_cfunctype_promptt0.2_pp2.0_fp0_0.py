import ctypes
# Test ctypes.CFUNCTYPE

import ctypes

# This is the prototype of the callback function.
# It takes an integer argument and returns nothing.
CALLBACKFUNC = ctypes.CFUNCTYPE(None, ctypes.c_int)

# This is the function that will be called from C.
def py_callback(arg):
    print("Callback called with argument %d" % arg)

# This is the C function that will call the callback.
# It takes a function pointer as first argument.
