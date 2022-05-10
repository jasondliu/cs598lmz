import ctypes
# Test ctypes.CFUNCTYPE.
#
# NOTE: The CFUNCTYPE() function is not available in Python 2.2, but
# this test is still run on Python 2.2 because the 'ctypes' module
# is available on Python 2.2.

import unittest
from test import test_support

class CFUNCTYPETestCase(unittest.TestCase):
    def test_callbacks(self):
        # Issue #5252: ctypes callback functions must be able to be
        # called more than once.
        cb = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x)
        self.assertEqual(cb(5), 5)
        self.assertEqual(cb(6), 6)
        self.assertEqual(cb(7), 7)
        self.assertEqual(cb(8), 8)
        self.assertEqual(cb(9), 9)
        self.assertEqual(cb(10), 10)

    def test_errcheck(self):
        # Issue #5252:
