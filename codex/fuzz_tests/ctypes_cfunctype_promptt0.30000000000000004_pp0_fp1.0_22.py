import ctypes
# Test ctypes.CFUNCTYPE

if os.name == "nt":
    import _ctypes_test
else:
    from ctypes import _ctypes_test

import unittest
from test import support

class CFunctionTypeTestCase(unittest.TestCase):

    def test_argtypes(self):
        # c_int(c_int, c_int)
        prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
        self.assertEqual(prototype.argtypes, (ctypes.c_int, ctypes.c_int))

        # c_int(c_int, c_int)
        prototype = ctypes.CFUNCTYPE(ctypes.c_int, (ctypes.c_int, ctypes.c_int))
        self.assertEqual(prototype.argtypes, (ctypes.c_int, ctypes.c_int))

        # c_int(c_int, c_int)
        prototype = ctypes.CFUNCTYPE(ctypes.
