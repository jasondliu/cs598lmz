import ctypes
# Test ctypes.CFUNCTYPE type.

import unittest
from test import support


@unittest.skipUnless(hasattr(ctypes, 'CFUNCTYPE'), 'requires ctypes')
class CFuncTypeTestCase(unittest.TestCase):
    def test_argtypes(self):
        # Check that the argtypes are converted to ctypes type objects.
        self.assertIsInstance(ctypes.CFUNCTYPE(None), ctypes.CFUNCTYPE)
        self.assertIsInstance(ctypes.CFUNCTYPE(None, None), ctypes.CFUNCTYPE)
        self.assertIsInstance(ctypes.CFUNCTYPE(None, ctypes.c_int),
                              ctypes.CFUNCTYPE)

    def test_restype(self):
        # Check that the restype is converted to a ctypes type object.
        self.assertIsInstance(ctypes.CFUNCTYPE(ctypes.c_int), ctypes.CFUNCTYPE)
        self.assertIsInstance(ctypes.CFUNCTYPE(
