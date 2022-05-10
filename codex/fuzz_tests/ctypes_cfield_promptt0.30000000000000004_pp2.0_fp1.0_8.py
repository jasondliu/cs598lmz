import ctypes
# Test ctypes.CField
#
# This test is a bit different from the other ctypes tests, because
# it doesn't use the ctypes module itself.  Instead, it uses the
# _ctypes module directly.  This is because the ctypes module is
# implemented in Python, and we want to test the C implementation.
#
# This test is also different from the other tests in that it doesn't
# use the test_support module.  This is because the test_support
# module is implemented in Python, and we want to test the C
# implementation.

import sys
import unittest

from _ctypes import __version__

class CFieldTestCase(unittest.TestCase):

    def test_CField(self):
        # This test is a bit different from the other ctypes tests, because
        # it doesn't use the ctypes module itself.  Instead, it uses the
        # _ctypes module directly.  This is because the ctypes module is
        # implemented in Python, and we want to test the C implementation.

        # This test is also different from the other tests in that it doesn't
        #
