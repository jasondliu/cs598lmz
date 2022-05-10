import ctypes
# Test ctypes.CField
class test_cfield(unittest.TestCase):
    def test_cfield(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]
        x = X()
        self.assertEqual(x.a, 0)
        self.assertEqual(x.b, 0)
        x.a = 42
        x.b = 24
        self.assertEqual(x.a, 42)
        self.assertEqual(x.b, 24)
        self.assertEqual(ctypes.sizeof(x), 8)
        self.assertEqual(ctypes.sizeof(X), 8)

    def test_cfield_in_union(self):
        class X(ctypes.Union):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]
        x = X()
        self.assertEqual(x.a, 0)
        self.assertEqual
