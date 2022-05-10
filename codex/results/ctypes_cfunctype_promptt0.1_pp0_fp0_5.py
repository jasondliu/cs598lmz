import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointer must have the following signature:
# int func(int)
CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the function to pass to the dll.
def callback(i):
    print('callback', i)
    return i + 42

# Call the dll function, passing callback.
lib.set_callback(CALLBACK(callback))

# Now call the function pointer stored inside the dll.
lib.call_callback(5)

# This should print:
# callback 5
# callback returned 47
