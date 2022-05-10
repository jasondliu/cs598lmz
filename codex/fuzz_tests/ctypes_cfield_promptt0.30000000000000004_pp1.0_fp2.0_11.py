import ctypes
# Test ctypes.CField
class CFieldTestCase(unittest.TestCase):
    def test_CField(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int, 1),
                        ("c", ctypes.c_int, 2),
                        ("d", ctypes.c_int, 3),
                        ("e", ctypes.c_int, 4),
                        ("f", ctypes.c_int, 5),
                        ("g", ctypes.c_int, 6),
                        ("h", ctypes.c_int, 7)]

        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.b.offset, 0)
        self.assertEqual(X.c.offset, 0)
        self.assertEqual(X.d.offset, 0)
        self.assertEqual(X.e.offset, 0)
        self.assertEqual(X.f.offset, 0)
        self.assertEqual(X.
