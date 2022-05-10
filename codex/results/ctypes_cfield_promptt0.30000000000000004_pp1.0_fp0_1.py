import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_CField(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]
        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.b.offset, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(ctypes.sizeof(X), 2 * ctypes.sizeof(ctypes.c_int))

    def test_CField_with_alignment(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]
            _pack_ = 1
        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.b.offset, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(ctypes.sizeof(
