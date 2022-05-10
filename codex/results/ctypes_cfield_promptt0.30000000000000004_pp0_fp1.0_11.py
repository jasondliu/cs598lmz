import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_CField(self):
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
                        ("j", ctypes.c_int)]
        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.b.offset, 4)
        self.assertEqual(X.c.offset, 8)
        self.assertEqual(X.d.offset, 12)
        self.assertEqual(X.e.offset, 16)
        self.assertEqual(X.f.offset, 20)

