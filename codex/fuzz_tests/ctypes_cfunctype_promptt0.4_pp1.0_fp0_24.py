import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointed to must have the same signature as
# CFUNCTYPE(c_int, c_int), that is c_int func(c_int).

# The prototype of the function is:
# c_int callit(c_int (*func)(c_int), c_int arg)
callit = lib.callit
callit.argtypes = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int), ctypes.c_int
callit.restype = ctypes.c_int

def func(arg):
    print('func', arg)
    return arg + 3

print(callit(func, 5))

# This is a function that returns a function pointer.
# The function returned must have the same signature as
# CFUNCTYPE(c_int, c_int), that is c_int func(c_int).

