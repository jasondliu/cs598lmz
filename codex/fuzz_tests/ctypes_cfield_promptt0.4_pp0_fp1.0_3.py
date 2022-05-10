import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_basic(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]
        self.assertEqual(ctypes.sizeof(X), ctypes.sizeof(ctypes.c_int)*2)
        self.assertEqual(X._fields_, [("a", ctypes.c_int), ("b", ctypes.c_int)])
        self.assertEqual(X._pack_, 1)
        self.assertEqual(X._anonymous_, [])

    def test_c_char_p(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_char_p)]
        self.assertEqual(ctypes.sizeof(X), ctypes.sizeof(ctypes.c_void_p))
        self.assertEqual(X._fields_, [("a", ctypes.c_char
