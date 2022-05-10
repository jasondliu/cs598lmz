import ctypes
# Test ctypes.CField
import ctypes
import unittest
from test import support

class Struct(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class CFieldTestCase(unittest.TestCase):
    def test_field_offset(self):
        self.assertEqual(ctypes.sizeof(ctypes.c_int),
                           ctypes.c_int.in_dll(Struct, "a").value)
        self.assertEqual(2 * ctypes.sizeof(ctypes.c_int),
                           ctypes.c_int.in_dll(Struct, "b").value)

def test_main():
    support.run_unittest(CFieldTestCase)

if __name__ == "__main__":
    test_main()
