import ctypes
# Test ctypes.CFUNCTYPE
#
# This test case is a little bit more complex than the others.
# It is not run automatically by the testsuite.  It is only run
# when the test is run with the -uall switch.
#
# The test creates a DLL with a function 'bar' which takes a
# callback function as an argument.  The callback function is
# called twice, once with a string, and once with an integer.
# The callback function must return the length of the string or
# integer.
#

from ctypes import *

# This is the prototype of the function in the DLL.

PROTOTYPE = CFUNCTYPE(c_int, c_char_p)

# This is the source code of the DLL:

