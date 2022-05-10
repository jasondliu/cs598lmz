import ctypes
# Test ctypes.CField
#

import unittest
from test import support

# XXX: some assertEqual()s call str() on arguments, so they fail
#      if the argument doesn't have a __str__() method.


class CFuncPtrTestCase(unittest.TestCase):
    def test_basic(self):
        import _ctypes_test
        dll = ctypes.CDLL(_ctypes_test.__file__)

        func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(("my_sqr", dll))
        self.assertEqual(func(5), 25)

        func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(("my_sqr2", dll))
        self.assertEqual(func(5), 25)

        func = ctypes.CFUNCTYPE(None, ctypes.c_int)(("my_sqr3", dll))
        func(5)

    def test_cache(self):
        import _ctypes
