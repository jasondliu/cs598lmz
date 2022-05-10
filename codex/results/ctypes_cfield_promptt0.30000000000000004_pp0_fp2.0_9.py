import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_CField(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int),
                        ("c", ctypes.c_int),
                        ("d", ctypes.c_int)]
            _anonymous_ = ["b", "c"]

        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.b.offset, 4)
        self.assertEqual(X.c.offset, 8)
        self.assertEqual(X.d.offset, 12)

        self.assertEqual(X.a.size, 4)
        self.assertEqual(X.b.size, 4)
        self.assertEqual(X.c.size, 4)
        self.assertEqual(X.d.size, 4)

        self.assertEqual(X.a.index, 0)
        self.assertEqual(X.b.
