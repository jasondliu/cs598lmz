import ctypes
# Test ctypes.CField
class CFieldTestCase(unittest.TestCase):
    def test_init(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]
        self.assertEqual(X._fields_, [("a", ctypes.c_int),
                                      ("b", ctypes.c_int)])
        self.assertEqual(X._pack_, 1)
        self.assertEqual(X.a, ctypes.c_int)
        self.assertEqual(X.b, ctypes.c_int)
        self.assertEqual(X._fields_, [("a", ctypes.c_int),
                                      ("b", ctypes.c_int)])
        self.assertEqual(X._pack_, 1)
        self.assertEqual(X.a, ctypes.c_int)
        self.assertEqual(X.b, ctypes.c_int)
        self.assertEqual(X.a
