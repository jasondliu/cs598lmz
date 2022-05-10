import ctypes
# Test ctypes.CField
from ctypes.test import is_resource_enabled

class X(ctypes.Structure):
    _fields_ = [("one", ctypes.c_int),
                ("two", ctypes.c_int),
                ("three", ctypes.c_int),
                ("four", ctypes.c_int),
                ]

    class _anonymous_1(ctypes.Union):
        _fields_ = [("a", ctypes.c_int),
                    ("b", ctypes.c_int),
                    ]

    class _anonymous_2(ctypes.Union):
        _fields_ = [("c", ctypes.c_int),
                    ("d", ctypes.c_int),
                    ]

    _anonymous_ = ("u1", "u2")
    _fields_ = [("u1", _anonymous_1),
                ("u2", _anonymous_2),
                ]

# Test if anonymous fields are set properly
class TestAnon(unittest.TestCase):
    def test_anon(self):
        x = X()
