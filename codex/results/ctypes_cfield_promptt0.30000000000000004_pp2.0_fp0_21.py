import ctypes
# Test ctypes.CField.from_address

import unittest
from test import support

class CFoo(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Test(unittest.TestCase):
    def test_from_address(self):
        foo = CFoo()
        foo.a = 1
        foo.b = 2
        self.assertEqual(foo.a, 1)
        self.assertEqual(foo.b, 2)
        self.assertEqual(foo.a, ctypes.c_int.from_address(id(foo)).value)
        self.assertEqual(foo.b, ctypes.c_int.from_address(id(foo) + ctypes.sizeof(ctypes.c_int)).value)

    def test_from_buffer(self):
        buf = ctypes.create_string_buffer(8)
        self.assertEqual(ctypes.c_int.from_buffer(buf).value, 0)
        self.assert
