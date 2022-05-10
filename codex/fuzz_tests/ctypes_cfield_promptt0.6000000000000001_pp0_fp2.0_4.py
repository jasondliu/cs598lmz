import ctypes
# Test ctypes.CField.from_address
import _ctypes_test
import unittest

class CFieldTestCase(unittest.TestCase):
    def test_from_address(self):
        f = _ctypes_test.MyStructure._fields_[0]
        self.assertEqual(f.from_address(id(f)).name, f.name)
        self.assertEqual(f.from_address(id(f)).offset, f.offset)
        self.assertEqual(f.from_address(id(f)).bitsize, f.bitsize)
        self.assertEqual(f.from_address(id(f)).bitshift, f.bitshift)
        self.assertEqual(f.from_address(id(f))._type_, f._type_)
        self.assertEqual(f.from_address(id(f))._length_, f._length_)
        self.assertEqual(f.from_address(id(f))._size_, f._size_)
        self.assertEqual(f.from_address(
