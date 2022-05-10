import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

lib = ctypes.CDLL(_ctypes_test.__file__)

# This is a function that takes a function pointer as argument.
# The function pointer must take an integer argument, and return
# an integer.

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# This is the function that we pass to the test function.

@CMPFUNC
def func(i):
    print("func", i)
    return i

# This is the function that we pass to the test function.

@CMPFUNC
def func2(i):
    print("func2", i)
    return i

# Call the test function.  This should print "func 42"

lib.pass_func(func, 42)

# Call the test function.  This should print "func2 42"

lib.pass_func(func2, 42)

# Call the test function.  This should print "func 42"

lib.pass_func(func
