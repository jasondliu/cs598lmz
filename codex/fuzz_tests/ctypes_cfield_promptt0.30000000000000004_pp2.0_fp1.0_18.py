import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_field_size(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]
        self.assertEqual(ctypes.sizeof(X), ctypes.sizeof(ctypes.c_int))

    def test_field_offset(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]
        self.assertEqual(ctypes.addressof(X.a), ctypes.addressof(X))

    def test_field_offset_2(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]
        self.assertEqual(ctypes.addressof(X.a), ctypes.addressof(X))
        self.assertEqual(ctypes.addressof(X.b), ctypes.addressof(X
