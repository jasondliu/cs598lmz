import ctypes
# Test ctypes.CField

class TestCField(unittest.TestCase):
    def test_cfield(self):
        class X(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int)]
        self.assertEqual(ctypes.sizeof(X), ctypes.sizeof(ctypes.c_int))
        self.assertEqual(X().x, 0)
        X.x.__set__(X(), 42)
        self.assertEqual(X().x, 42)
        self.assertEqual(X.x.__get__(X()), 42)

    def test_cfield_in_union(self):
        class X(ctypes.Union):
            _fields_ = [("x", ctypes.c_int)]
        self.assertEqual(ctypes.sizeof(X), ctypes.sizeof(ctypes.c_int))
        self.assertEqual(X().x, 0)
        X.x.__set__(X(), 42)
        self.assertEqual(X().x, 42)
