import ctypes
# Test ctypes.CFUNCTYPE
#
# This is the same as the test_cfunctype.py test, except that we use
# ctypes.CFUNCTYPE to create the callback function type.  This is
# important because ctypes.CFUNCTYPE is a Python-level function, and
# the callback function type is a C-level function.
#
# The test_cfunctype.py test is in the same directory as this file,
# and is run by the same test suite.

import unittest
