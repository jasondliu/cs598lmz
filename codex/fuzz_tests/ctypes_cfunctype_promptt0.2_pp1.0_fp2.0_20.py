import ctypes
# Test ctypes.CFUNCTYPE()

# This test is for issue #14091

import ctypes
from ctypes import *

def test_CFUNCTYPE():
    # This is the function we want to call
    def func(x):
        return x + 1

    # This is the function type we want to use
    CFUNCTYPE_func = CFUNCTYPE(c_int, c_int)

    # This is the function we want to call
    def func2(x):
        return x + 2

    # This is the function type we want to use
    CFUNCTYPE_func2 = CFUNCTYPE(c_int, c_int)

    # This is the function we want to call
    def func3(x):
        return x + 3

    # This is the function type we want to use
    CFUNCTYPE_func3 = CFUNCTYPE(c_int, c_int)

    # This is the function we want to call
    def func4(x):
        return x + 4

    # This is the function type we want to
