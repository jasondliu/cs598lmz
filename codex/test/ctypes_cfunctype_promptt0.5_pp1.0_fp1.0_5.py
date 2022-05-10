import ctypes
# Test ctypes.CFUNCTYPE
#
# This test is intended to exercise the ctypes.CFUNCTYPE()
# functionality.
#
# It is a very simple test and only exercises a small number of
# functions.
#
# The tests are designed to be run manually by a developer and not
# as part of the automated testing.
#
# This test is designed to be run on a system with a 32 bit
# architecture.
#

#
# This function is used to test ctypes.CFUNCTYPE().
#
# The function takes an integer, adds one to it and returns the
# result.
#
# This function is used by test_cfunc_1() to test ctypes.CFUNCTYPE().
#
# The function is also used by test_cfunc_2() to test how ctypes.CFUNCTYPE()
# handles a function that takes a pointer as an argument.
#
def cfunc_1(x):
    return x+1

#
# This function is used to test ctypes.CFUNCTYPE().
#
# The function takes an integer pointer, adds one
