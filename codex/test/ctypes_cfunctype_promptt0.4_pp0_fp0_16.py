import ctypes
# Test ctypes.CFUNCTYPE
#
# This test is not complete.  It only checks that a few basic things work.

import unittest

from ctypes import *

class CFuncPtrTestCase(unittest.TestCase):

    def test_basic(self):
        f = CFUNCTYPE(c_int, c_int)
        self.assertEqual(f.__name__, "CFUNCTYPE(c_int, c_int)")
        self.assertEqual(f.argtypes, (c_int,))
        self.assertEqual(f.restype, c_int)

        f = CFUNCTYPE(c_int, c_int, c_int, c_int)
        self.assertEqual(f.__name__, "CFUNCTYPE(c_int, c_int, c_int, c_int)")
        self.assertEqual(f.argtypes, (c_int, c_int, c_int))
        self.assertEqual(f.restype, c_int)

