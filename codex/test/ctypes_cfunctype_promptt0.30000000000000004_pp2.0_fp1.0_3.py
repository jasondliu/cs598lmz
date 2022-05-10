import ctypes
# Test ctypes.CFUNCTYPE
#
# This test is based on the test_ctypes.py test_callbacks test.
#
# This test is intended to be run from the Python build directory with:
# ./python Lib/test/regrtest.py test_ctypes_callbacks
#
# It is expected to fail with a segfault when run with the system Python.

import unittest
