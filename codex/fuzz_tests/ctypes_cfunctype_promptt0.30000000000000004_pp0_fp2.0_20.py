import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = CDLL(_ctypes_test.__file__)

# This is a function with a callback argument.  The callback
# argument must be a function with an int argument and no return
# value.

CALLBACK = CFUNCTYPE(None, c_int)

# This is the function we want to call.  It takes a function pointer
# as first argument, and an integer as second argument.

prototype = CFUNCTYPE(c_int, CALLBACK, c_int)
paramflags = (1, "func", 0), (1, "value", 0)

# Set the paramflags
prototype.errcheck = lambda result, func, value: result

func = prototype(( "callback", lib ), paramflags)

# This is the function to be called by the callback function.
# It prints the value passed to it.

def py_callback(value):
    print("py_callback called with", value)

# Call the function.  The integer argument is passed to the
# callback.

func(CALLBACK(
