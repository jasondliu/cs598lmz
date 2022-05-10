import ctypes
# Test ctypes.CField.
#

import ctypes
import unittest

class Test(unittest.TestCase):

    def test_simple(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_double),
                        ("b", ctypes.c_long),
                        ("c", ctypes.c_int),
                        ("d", ctypes.c_char),
                        ("e", ctypes.c_char),
                        ("f", ctypes.c_char),
                        ("g", ctypes.c_char),
                        ("h", ctypes.c_char),
                        ("i", ctypes.c_char),
                        ("j", ctypes.c_char),
                        ("k", ctypes.c_char),
                        ("l", ctypes.c_char),
                        ("m", ctypes.c_char),
                        ("n", ctypes.c_char),
                        ("o", ctypes.c_char),
                        ("p", ctypes.c_char),
                        ("q", ctypes.c_char),
                       
