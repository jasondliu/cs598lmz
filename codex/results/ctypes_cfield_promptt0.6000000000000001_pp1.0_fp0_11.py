import ctypes
# Test ctypes.CField
class MyStruct(ctypes.Structure):
    _fields_ = [ ("a", ctypes.c_int),
                 ("b", ctypes.c_int),
                 ( "c", ctypes.c_int, 1),
                 ( "d", ctypes.c_int, 2),
                 ( "e", ctypes.c_int, 0),
                 ( "f", ctypes.c_int, 3),
                 ( "g", ctypes.c_int, 0),
                 ( "h", ctypes.c_int, 1),
                 ( "i", ctypes.c_int, 0),
                 ( "j", ctypes.c_int, 3),
                 ( "k", ctypes.c_int, 0),
                 ( "l", ctypes.c_int, 1),
                 ( "m", ctypes.c_int, 0),
                 ( "n", ctypes.c_int, 3),
                 ]

import unittest

class Test(unittest.TestCase):
    def test_packing(self):
        # test that bit
