import ctypes
# Test ctypes.CField

class TestCField(unittest.TestCase):
    def test_simple(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int, 2)]
        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.a.size, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(X.b.offset, 4)
        self.assertEqual(X.b.size, 2)

    def test_more(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int, 2),
                        ("c", ctypes.c_int, 3)]
        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.a.size, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(
