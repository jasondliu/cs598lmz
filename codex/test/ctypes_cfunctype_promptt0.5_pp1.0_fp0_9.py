import ctypes
# Test ctypes.CFUNCTYPE
#
# Note:
#   This test is mostly copied from the Python test suite.
#   (Lib/test/test_ctypes/test_callbacks.py)
#
#   The reason for copying this test is to ensure that the
#   CFUNCTYPE functionality is working correctly.
#
#   The only modifications made to the test are to add a
#   call to run_test and to add the run_test function itself.

import unittest
