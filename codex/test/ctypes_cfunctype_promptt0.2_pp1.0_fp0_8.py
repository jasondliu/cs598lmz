import ctypes
# Test ctypes.CFUNCTYPE

from ctypes import *

def func(x):
    return x + 1

# Create a function type with one argument, and one result.
# The result type is c_int, the argument type is POINTER(c_int)
# because we want to pass a pointer.
CMPFUNC = CFUNCTYPE(c_int, POINTER(c_int))

# Convert the Python function into this C function pointer.
cmp_func = CMPFUNC(func)

# Now we can pass the function pointer to C code.
# The argtypes of the C function must match the types of the
# arguments we pass to the function.

# The following C code is compiled into a dynamic library using
# the supplied setup.py.  This library is then loaded.

# #include <stdio.h>
#
# int call_func(int (*cmp_func)(int *))
# {
#     int x = 99;
#     return cmp_func(&x);
# }

# Load the library, and retrieve the function called 'call_func'
