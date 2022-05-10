import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointer must take an integer argument and return
# an integer.

# The prototype of the function pointer is:
# int func(int)

FUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the function that will be passed to the "callback"
# function.

def py_func(arg):
    print("py_func", arg)
    return arg

# This is the function that takes a function pointer as argument.
# It is called "callback" in the C code.

callback = lib.callback
callback.argtypes = (FUNC,)
callback.restype = ctypes.c_int

# Now call the C function, passing our Python function as argument.

res = callback(FUNC(py_func))
print(res)

# Now call the C function again, passing a function pointer
#
