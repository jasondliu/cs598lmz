import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_c_field(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]

        class Y(ctypes.Union):
            _fields_ = [("x", X), ("p", ctypes.POINTER(ctypes.c_int))]

        self.assertEqual(X.a.offset, 0)
        self.assertEqual(Y.x.offset, 0)
        self.assertEqual(Y.p.offset, 0)

    def test_c_field_from_void_p(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_void_p)]

        class Y(ctypes.Union):
            _fields_ = [("x", X), ("p", ctypes.POINTER(ctypes.c_int))]

        self.assertEqual(X.a.offset, 0)
        self
