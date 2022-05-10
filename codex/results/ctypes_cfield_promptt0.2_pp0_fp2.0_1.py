import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_CField(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]
        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.b.offset, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(X.a.size, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(X.b.size, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(X.a.index, 0)
        self.assertEqual(X.b.index, 1)

    def test_CField_with_bitfields(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int, 1),
                        ("b", ctypes.c_int, 2),
                        ("c",
