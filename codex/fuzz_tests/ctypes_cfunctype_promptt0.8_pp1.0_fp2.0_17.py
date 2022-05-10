import ctypes
# Test ctypes.CFUNCTYPE
#
# <hans@at.or.at>
#

import unittest
from test import test_support

class CFunctionTypeTestCase(unittest.TestCase):
    def test_ellipsis(self):
        cfunc = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int,
                                 ctypes.c_int, ctypes.c_int, ctypes.c_int,
                                 ctypes.c_int, ctypes.c_int)
        f = cfunc(lambda: None)
        if f.argtypes is None:
            self.assertRaises(TypeError, f, 1, 2)
            return

        self.assertEqual(f.argtypes,
                         (ctypes.c_int, ctypes.c_int, ctypes.c_int,
                          ct
