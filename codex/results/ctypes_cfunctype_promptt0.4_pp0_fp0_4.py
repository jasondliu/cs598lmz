import ctypes
# Test ctypes.CFUNCTYPE
import _ctypes_test

try:
    import _ctypes_test
except ImportError:
    raise ImportError("This test requires _ctypes_test module")

if sys.platform == "win32":
    from _ctypes_test import WINFUNCTYPE
else:
    from _ctypes_test import CFUNCTYPE as WINFUNCTYPE

import unittest
from test import support

class CFuncPtrTestCase(unittest.TestCase):

    def test_basic(self):
        # Check the type of CFUNCTYPE(c_int)(lambda: 42)
        f = ctypes.CFUNCTYPE(ctypes.c_int)(lambda: 42)
        self.assertEqual(f(), 42)
        self.assertEqual(f.__class__, ctypes._CFuncPtr)

    def test_restype_none(self):
        # Check the type of CFUNCTYPE(None)(lambda: None)
        f = ctypes.CFUNCTYPE(None)(lambda: None)
        self
