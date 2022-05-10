import ctypes
# Test ctypes.CField and ctypes.StructField
import unittest
from test import test_support as support

class FieldTestCase(unittest.TestCase):

    def test_CField(self):
        from ctypes import c_int
        class X(ctypes.Structure):
            _fields_ = [("a", c_int), ("b", c_int)]

        self.assertEqual(str(X._fields_[0]), "<Field type=c_int, ofs=0, size=4>")

        self.assertEqual(X._fields_[0].ofs, 0)
        self.assertEqual(X._fields_[1].ofs, 4)

        self.assertEqual(X._fields_[0].size, 4)
        self.assertEqual(X._fields_[1].size, 4)

        self.assertEqual(X._fields_[0].offset, 0)
        self.assertEqual(X._fields_[1].offset, 4)

    def test_StructField(self):
        class X(ctypes.Structure
