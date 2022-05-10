import ctypes
# Test ctypes.CField

class TestCField:
    def test_simple(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]
        self.assertEqual(X._fields_, [("a", ctypes.c_int)])

    def test_int(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int),
                        ("c", ctypes.c_int),
                        ("d", ctypes.c_int),
                        ("e", ctypes.c_int),
                        ("f", ctypes.c_int),
                        ("g", ctypes.c_int),
                        ("h", ctypes.c_int),
                        ("i", ctypes.c_int),
                        ("j", ctypes.c_int),
                        ("k", ctypes.c_int),
                        ("l", ctypes.c_int),
                        ("m", ctypes.c_int),
                        ("n", c
