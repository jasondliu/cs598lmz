import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointer must have the following signature:
# int func(double)
CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_double)

# This is the function to pass to the callback function.
def py_callback(arg):
    print 'called back with', arg
    return 42

# Convert the Python function into a function pointer.
cb_func = CALLBACK(py_callback)

# Now pass the function pointer to the C callback function.
lib.set_callback(cb_func)

# Now call the C callback function.
res = lib.call_callback(3.14)
print 'result', res
