import ctypes
# Test ctypes.CFUNCTYPE
#
# This test is based on the test_ctypes.py test_cfunctype test.
#
# The only difference is that the function is called with a
# different number of arguments.
#
# The bug was that the function was called with the wrong number
# of arguments, and the wrong number of arguments was passed to
# the function.

import unittest
