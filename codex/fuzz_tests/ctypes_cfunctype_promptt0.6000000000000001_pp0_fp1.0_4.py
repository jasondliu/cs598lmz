import ctypes
# Test ctypes.CFUNCTYPE.
# This should have no crashes.
from ctypes import *
from ctypes.test import need_symbol
import _ctypes_test

#
# test with simple functions
#

# define a simple function taking no arguments and returning an integer
def func(*args):
    return 42

# create an instance of CFUNCTYPE
CMPFUNC = CFUNCTYPE(c_int)

# call the instance
assert CMPFUNC(func)() == 42

#
# test with callback functions
#

# define a function taking a function and returning the result of a call
# to this function
def func_with_callback(func, a, b):
    return func(a, b)

# define a function taking two integers and returning an integer
def func_with_callback_inner(a, b):
    return a + b

# create an instance of CFUNCTYPE
CMPFUNC = CFUNCTYPE(c_int, c_int, c_int)

# call the instance
assert func_with_callback(CMPFUN
