import ctypes
# Test ctypes.CField()
class TestCField(unittest.TestCase):
    def test_CField(self):
        # Test ctypes.CField()
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int, 4),
                        ("c", ctypes.c_int, 2)]

        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.b.offset, 4)
        self.assertEqual(X.c.offset, 6)
        self.assertEqual(ctypes.sizeof(X), 8)

        self.assertEqual(X.a.size, 4)
        self.assertEqual(X.b.size, 1)
        self.assertEqual(X.c.size, 1)

        self.assertEqual(X.a.index, 0)
        self.assertEqual(X.b.index, 1)
        self.assertEqual(X.c.index, 2)

        self.
