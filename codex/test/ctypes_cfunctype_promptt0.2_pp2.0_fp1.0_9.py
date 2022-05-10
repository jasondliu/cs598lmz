import ctypes
# Test ctypes.CFUNCTYPE()

# This test is a bit tricky, because it has to work on both Python 2 and 3.
# On Python 2, the ctypes module is written in Python, and the CFUNCTYPE()
# function is implemented in Python.  On Python 3, the ctypes module is
# written in C, and the CFUNCTYPE() function is implemented in C.
#
# The Python 2 implementation of CFUNCTYPE() is not very robust, and
# doesn't handle all the cases that the C implementation does.  So we
# have to be careful to test only cases that work on both Python 2 and 3.

import sys
import unittest
