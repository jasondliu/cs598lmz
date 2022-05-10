import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_CField(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int, 1),
                        ("b", ctypes.c_int, 2),
                        ("c", ctypes.c_int, 3),
                        ("d", ctypes.c_int, 4),
                        ("e", ctypes.c_int, 5),
                        ("f", ctypes.c_int, 6),
                        ("g", ctypes.c_int, 7),
                        ("h", ctypes.c_int, 8),
                        ("i", ctypes.c_int, 9),
                        ("j", ctypes.c_int, 10),
                        ("k", ctypes.c_int, 11),
                        ("l", ctypes.c_int, 12),
                        ("m", ctypes.c_int, 13),
                        ("n", ctypes.c_int, 14),
                        ("o", ctypes.c_int, 15),
                        ("p", ctypes
