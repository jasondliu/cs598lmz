import ctypes
# Test ctypes.CField and ctypes.Field
import unittest

# example for a C structure
class struct_test(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int)]

class CFieldTest(unittest.TestCase):
    def test_CField_instance(self):
        f = ctypes.CField(None, ctypes.c_int, 'a')
        self.assertEqual(f._name, 'a')
        self.assertEqual(f._type, ctypes.c_int)
        self.assertEqual(f.offset, 0)
        self.assertEqual(f.size, 4)
        self.assertEqual(f.index, 0)
        self.assertEqual(f.pack, 1)
        self.assertEqual(f.alignment, 4)
        self.assertEqual(repr(f), "CField(None, c_int, 'a')")

    def test_CField_instance_offset(self):
        f = ctypes.CField(None, ctypes.
