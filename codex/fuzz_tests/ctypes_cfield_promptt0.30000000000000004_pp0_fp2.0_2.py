import ctypes
# Test ctypes.CField

class CFieldTestCase(unittest.TestCase):
    def test_field_sizeof(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_short)]
        self.assertEqual(ctypes.sizeof(X), 8)

    def test_field_offsetof(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_short)]
        self.assertEqual(ctypes.sizeof(X), 8)

    def test_field_offsetof_non_contiguous(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_short),
                        ("c", ctypes.c_short)]
        self.assertEqual(ctypes.sizeof(X), 8)

    def test_field_offsetof_non_contiguous
