import ctypes
# Test ctypes.CField
class CFieldTest(unittest.TestCase):
    def test_cfield(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]
        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.b.offset, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(ctypes.sizeof(X), 2 * ctypes.sizeof(ctypes.c_int))
        self.assertEqual(ctypes.alignment(X), ctypes.alignment(ctypes.c_int))

    def test_cfield_with_offset(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int, 1),
                        ("b", ctypes.c_int, 1)]
        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.b.offset, 1)
