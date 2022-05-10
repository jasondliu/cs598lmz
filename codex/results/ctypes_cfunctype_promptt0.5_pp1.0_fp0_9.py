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
from test import support
from ctypes import *
from ctypes.test import needs_sgi_dll

# The original test code is not Python 3 compatible.
# This test is only run for Python 2.
@unittest.skipUnless(sys.version_info[0] < 3, 'Python 3 test')
class CFuncPtrTestCase(unittest.TestCase):

    # CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)
    #
    # restype
    #   The result type.  This must be a ctypes type.
   
