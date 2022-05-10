import ctypes
# Test ctypes.CField

class TestCField(unittest.TestCase):
    def test_simple(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]

        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.a.size, ctypes.sizeof(ctypes.c_int))

    def test_nested(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]

        class Y(ctypes.Structure):
            _fields_ = [("b", X)]

        self.assertEqual(Y.b.offset, 0)
        self.assertEqual(Y.b.size, ctypes.sizeof(X))
        self.assertEqual(Y.b.a.offset, 0)
        self.assertEqual(Y.b.a.size, ctypes.sizeof(ctypes.c_int))

    def test_array(self):
        class X(ctypes
