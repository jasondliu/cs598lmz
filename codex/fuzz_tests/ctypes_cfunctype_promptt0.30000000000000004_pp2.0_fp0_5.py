import ctypes
# Test ctypes.CFUNCTYPE()

# This test is based on the test_callbacks.py test.

import unittest
from test import test_support

class CFuncPtrTestCase(unittest.TestCase):
    def callback(self, *args):
        self.got_args = args
        return args[-1]

    def test_basic(self):
        # CFUNCTYPE() with no argtypes or restype specified
        # should default to int arguments and return type.
        cb = ctypes.CFUNCTYPE(None)(self.callback)
        self.assertEqual(cb(1), 1)
        self.assertEqual(self.got_args, (1,))

        # Now specify an explicit restype
        cb = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)(self.callback)
        self.assertEqual(cb(1.5), 1.5)
        self.assertEqual(self.got_args, (1.5,))

        # Now specify argtypes too
        cb
