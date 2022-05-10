import ctypes
# Test ctypes.CFUNCTYPE
#
# A simple example, with a Python function, that is passed as a callback
# function to C.
# The callback function is called repeatedly.
#
# This test is a bit strange, in that it tests that a ctypes function
# can be called from an external DLL without causing an access violation,
# but the test cannot actually be run from a Python test suite under
# Windows.

# To run this test, compile this file into a DLL, compile the other
# file into an EXE, and run the EXE.

# This file is compiled into a DLL, and the function 'test' is exported.
# The function 'test' does a 'CFUNCTYPE' of the function pointer given,
# and calls it repeatedly.  The Python function called will print a
# message on each call, to indicate that it is still alive.
#
# The other file defines a Python function, and calls 'test' to pass
# the Python function as a callback.
#
# The EXE can be run from the command line, or from the IDLE shell.

from ctypes import *

#
