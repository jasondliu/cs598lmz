import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument
# and calls it.
CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the function that should be called by the callback
def py_callback(arg):
    print("callback called with argument", arg)
    return arg + 42

# This is the function that calls the callback
def call_callback(func, arg):
    return func(arg)

# Convert the Python function to a C function pointer
c_callback = CALLBACK(py_callback)

# Convert the Python function to a C function pointer
