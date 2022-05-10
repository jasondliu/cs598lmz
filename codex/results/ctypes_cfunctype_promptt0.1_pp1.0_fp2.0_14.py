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
    print('callback called with argument', arg)
    return 42

# Convert the Python function into a function pointer.
c_callback = CALLBACK(py_callback)

# Now call the C function, which will in turn call our callback.
lib.set_callback(c_callback)

# This will cause the callback to be called.
lib.call_callback(3.14)

# Now test that the callback can be called from another thread.
import threading

def call_in_other_thread():
    lib.call_callback(2.78)

# Start a thread that will call the callback.

