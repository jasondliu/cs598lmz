import ctypes
# Test ctypes.CField

class TestCField(unittest.TestCase):
    def test_CField_simple(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]

        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.b.offset, ctypes.sizeof(ctypes.c_int))

    def test_CField_simple_offsets(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int, 1),
                        ("b", ctypes.c_int, 1)]

        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.b.offset, ctypes.sizeof(ctypes.c_int))

    def test_CField_simple_padding(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int, 1),

