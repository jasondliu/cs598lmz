import ctypes
# Test ctypes.CField.

import unittest

class CFieldTest(unittest.TestCase):

    class test_class(ctypes.Structure):
        _fields_ = [("a", ctypes.c_long),
                    ("b", ctypes.c_long),
                    ("c", ctypes.c_long),
                    ("d", ctypes.c_long),
                    ("e", ctypes.c_long),
                    ("f", ctypes.c_long),
                    ("g", ctypes.c_long),
                    ("h", ctypes.c_long),
                    ("i", ctypes.c_long),
                    ("j", ctypes.c_long)]

    def test_offset(self):
        # check that the offsets are the same as what struct.calcsize() returns
        import struct
        class X(self.test_class):
            _pack_ = 4
        self.assertEqual(ctypes.sizeof(X), struct.calcsize("l"*10))

    def test_get_set_address(self):
        # check that _get
