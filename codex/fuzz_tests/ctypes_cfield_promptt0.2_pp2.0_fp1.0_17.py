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
        self.assertEqual(ctypes.addressof(X.a), ctypes.addressof(X.b) - ctypes.sizeof(ctypes.c_int))
        self.assertEqual(ctypes.addressof(X.b), ctypes.addressof(X.a) + ctypes.sizeof(ctypes.c_int))

    def test_CField_in_Union(self):
        class X(ctypes.Union):
            _fields_ = [
