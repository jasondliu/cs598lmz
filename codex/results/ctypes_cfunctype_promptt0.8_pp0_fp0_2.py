import ctypes
# Test ctypes.CFUNCTYPE(T).from_address(T)
#
# This test is to check that from_address() works for
# all callable ctypes types (ctypes function, ctypes instance method,
# ctypes class method, ctypes static method).

import unittest
from test import support
from ctypes import *
from ctypes.test import is_resource_enabled

libc = CDLL(support.dlpath("ctypes_test"))

class CFunctionTypeTestCase(unittest.TestCase):
    def test_CFuncPtr(self):
        self.assertEqual(sizeof(CFuncPtr), sizeof(c_void_p))

        code = "int printf(const char *fmt, ...);"
        printf = CFUNCTYPE(c_int, c_char_p)(("printf", libc),
                                            (c_char_p,))
        self.assertEqual(printf("%d", 42), 2)

        addr = addressof(printf)
        self.assertEqual(CFUNCTYPE(c_int, c_char
