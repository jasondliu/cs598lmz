import ctypes
# Test ctypes.CField
class CFieldTestCase(unittest.TestCase):
    def test_fields(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]

        self.assertEqual(X._fields_, [("a", ctypes.c_int), ("b", ctypes.c_int)])
        self.assertEqual(X._pack_, 1)
        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.b.offset, ctypes.sizeof(ctypes.c_int))

    def test_fields2(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int),
                        ("c", ctypes.c_double)]

        self.assertEqual(X._fields_, [("a", ctypes.c_int), ("b", ctypes.c_int), ("c", c
