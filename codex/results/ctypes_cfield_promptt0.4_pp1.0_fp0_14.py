import ctypes
# Test ctypes.CField
class TestCField:
    def test_simple(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int, 1),
                        ("c", ctypes.c_int, 1, 3),
                        ("d", ctypes.c_int, 1, 3),
                        ("e", ctypes.c_int, 1, 3),
                        ("f", ctypes.c_int, 1, 3),
                        ("g", ctypes.c_int, 1, 3),
                        ("h", ctypes.c_int, 1, 3),
                        ("i", ctypes.c_int, 1, 3),
                        ("j", ctypes.c_int, 1, 3),
                        ("k", ctypes.c_int, 1, 3),
                        ("l", ctypes.c_int, 1, 3),
                        ("m", ctypes.c_int, 1, 3),
                        ("n", ctypes.c_int, 1, 3),
                        ("o", ctypes
