import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointer must have the same signature as the
# CFUNCTYPE function we pass.

# The prototype of the function is:
# int function(int(*)(int))

FUNCTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# The function must be registered with a prototype, so that
# the argtypes can be set.

lib.set_callback.argtypes = FUNCTYPE,

# The callback must be a ctypes function, not a Python callable.

def callback(arg):
    print("callback called with", arg)
    return arg + 1

# Now we can pass the callback to the C function.

lib.set_callback(FUNCTYPE(callback))

# Now we can call the C function.  It will call our callback.

lib.call_callback(5)

#
