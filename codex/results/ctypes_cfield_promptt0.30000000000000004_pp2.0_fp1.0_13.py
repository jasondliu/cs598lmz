import ctypes
# Test ctypes.CField

class TestCField(unittest.TestCase):

    def test_simple(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]
        self.assertEqual(ctypes.sizeof(X), ctypes.sizeof(ctypes.c_int) * 2)

        class Y(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int, 1),
                        ("c", ctypes.c_int, 2),
                        ("d", ctypes.c_int, 3),
                        ("e", ctypes.c_int, 4),
                        ("f", ctypes.c_int, 5),
                        ("g", ctypes.c_int, 6),
                        ("h", ctypes.c_int, 7),
                        ("i", ctypes.c_int, 8),
                        ("j", ctypes.c_int, 9),
                        ("k", ctypes
