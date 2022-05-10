import ctypes
# Test ctypes.CFUNCTYPE
#
# This test is based on the test_ctypes.py test_cfunctype test.
#
# The test_cfunctype test is based on the ctypes tutorial, section
# "Passing callbacks to C".
#
# The ctypes tutorial is Copyright (c) 2001-2006 Thomas Heller.  All
# rights reserved.  It is licensed under the Python Software
# Foundation License.

from ctypes import *

# This is the prototype of the callback function.
CALLBACKFUNC = CFUNCTYPE(c_int, c_int, c_int)

# This is the prototype of the C function that takes a callback as
# an argument.
CFUNC = CFUNCTYPE(None, CALLBACKFUNC, c_int)

# This is the C function that takes a callback as an argument.
def c_func(func, arg):
    return func(arg, arg)

# This is the Python callback function.
def py_func(a, b):
    return a + b

# This is the Python function that calls the C function
