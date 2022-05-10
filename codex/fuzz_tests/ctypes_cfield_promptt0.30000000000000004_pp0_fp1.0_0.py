import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_cfield(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]
        self.assertEqual(ctypes.sizeof(X), 8)
        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.b.offset, 4)
        self.assertEqual(X.a.size, 4)
        self.assertEqual(X.b.size, 4)

    def test_cfield_subclass(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]
        class Y(X):
            _fields_ = [("c", ctypes.c_int)]
        self.assertEqual(ctypes.sizeof(Y), 12)
        self.assertEqual(Y.a.offset, 0)
