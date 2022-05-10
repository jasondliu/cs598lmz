import ctypes
# Test ctypes.CFUNCTYPE

import sys
import unittest
from test import support

class CFuncPtrTestCase(unittest.TestCase):

    def test_callbacks(self):
        # Issue #902
        f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x + 1)
        self.assertEqual(f(41), 42)

        # Issue #902
        f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x + 1)
        self.assertEqual(f(41), 42)

        # Issue #902
        f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x + 1)
        self.assertEqual(f(41), 42)

        # Issue #902
        f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x + 1)
        self.assertEqual(f
