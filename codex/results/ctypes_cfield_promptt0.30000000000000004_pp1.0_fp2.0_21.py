import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_cfield(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]
        self.assertEqual(ctypes.sizeof(X), 8)
        self.assertEqual(ctypes.alignment(X), 4)
        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.b.offset, 4)
        self.assertEqual(X.a.size, 4)
        self.assertEqual(X.b.size, 4)
        self.assertEqual(X.a.alignment, 4)
        self.assertEqual(X.b.alignment, 4)
        self.assertEqual(X.a.name, "a")
        self.assertEqual(X.b.name, "b")
        self.assertEqual(X.a.ctype, ctypes.c_int)
        self
