import ctypes
# Test ctypes.CFUNCTYPE

from ctypes import *
import sys

# This is a list of functions that are called with a function
# pointer as argument.
testfuncs = [cdll.msvcrt.printf, cdll.msvcrt.fprintf, cdll.msvcrt.sprintf]

def test(verbose=True):
    # Create a function that we can pass to the C functions
    def func(format, arg1, arg2, arg3):
        if verbose:
            print 'func called with', format, arg1, arg2, arg3
        return 0

    # Create a function pointer instance
    Callable = CFUNCTYPE(c_int, c_char_p, c_int, c_int, c_int)
    funcptr = Callable(func)

    for testfunc in testfuncs:
        # Call the testfunc with funcptr as argument.
        if verbose:
            print "calling", testfunc.__name__
        result = testfunc(funcptr, b"%s %s %s %s\n", 1, 2
