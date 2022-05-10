import ctypes
# Test ctypes.CField
class CFieldTestCase(unittest.TestCase):
    def test_cfield(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]
        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.b.offset, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(ctypes.sizeof(X), 2 * ctypes.sizeof(ctypes.c_int))

    def test_cfield_anonymous(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("", ctypes.c_int),
                        ("b", ctypes.c_int)]
        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.b.offset, 2 * ctypes.sizeof(ctypes.c_int))
        self.assertEqual(ct
