import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointed to must take an integer argument, and return
# an integer.

# The prototype is:
# int callit(int (*func)(int), int arg)
callit = lib.callit
callit.argtypes = (ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int),
                   ctypes.c_int)
callit.restype = ctypes.c_int

# This is the function that will be passed to callit:
def func(arg):
    return arg * 2

# This is the function type that will be used to create the
# function pointer.
FUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# Create the function pointer from the python function.
cfunc = FUNC(func)

# Now call callit:
res = callit(cfunc
