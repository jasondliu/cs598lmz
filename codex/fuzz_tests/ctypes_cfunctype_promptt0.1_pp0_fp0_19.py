import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointed to must return an int, and take two ints
# as arguments.

# The prototype of the function is:
# int callit(int (*func)(int, int), int arg1, int arg2)

callit = lib.callit
callit.argtypes = (ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int),
                   ctypes.c_int, ctypes.c_int)
callit.restype = ctypes.c_int

# This is the function that will be passed to callit():

def func(arg1, arg2):
    print("func", arg1, arg2)
    return arg1 + arg2

# Now call callit():

print(callit(func, 1, 2))

# Now call callit() with a function that takes more arguments than

