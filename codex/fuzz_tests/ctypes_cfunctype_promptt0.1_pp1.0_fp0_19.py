import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as an argument
# and calls it.
CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the function that will be called by the function pointer.
def py_callback(arg):
    print("callback called with argument", arg)
    return arg + 42

# This is the function that takes a function pointer as an argument.
# It returns the result of calling the function pointer.
lib.call_callback.argtypes = (CALLBACK,)
lib.call_callback.restype = ctypes.c_int

# Call the function with the function pointer.
res = lib.call_callback(CALLBACK(py_callback))
print("callback returned", res)

# This is a function that takes a function pointer as an argument
# and calls it.
CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, c
