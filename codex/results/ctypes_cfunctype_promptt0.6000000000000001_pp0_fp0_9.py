import ctypes
# Test ctypes.CFUNCTYPE
#
# This test is designed to make sure that CFUNCTYPE works with
# all calling conventions, and that it correctly converts Python
# return values to C return values.
#
# By passing arguments to the function we make sure that argtypes
# and restype are correctly used.

from ctypes import *

# The following functions are used for test purposes only.  Don't
# call them directly.

# void_func and void_func_caller:
# Make sure that CFUNCTYPE(None) works.

def void_func():
    pass

def void_func_caller(callback):
    callback()

# int_func and int_func_caller:
# Make sure that CFUNCTYPE(c_int) works.

def int_func():
    return 42

def int_func_caller(callback):
    return callback()

# string_func and string_func_caller:
# Make sure that CFUNCTYPE(c_char_p) works.

def string_func():
    return "Hello World"
