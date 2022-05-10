import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_basic(self):
        from _ctypes import CField, Field
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_char),
                        ("c", ctypes.c_double),
                        ("d", ctypes.c_longlong)]
        self.assertEqual(Field(X, "a").offset, 0)
        self.assertEqual(Field(X, "d").offset, 16)

    def test_subclass(self):
        from _ctypes import CField, Field
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_char),
                        ("c", ctypes.c_double),
                        ("d", ctypes.c_longlong)]
        class Y(X):
            _fields_ = [("e", ctypes.c_int),
                        ("f", ctypes.c_
