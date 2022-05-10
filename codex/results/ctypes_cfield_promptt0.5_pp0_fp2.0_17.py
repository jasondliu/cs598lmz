import ctypes
# Test ctypes.CField
class CFieldTestBase(unittest.TestCase):
    def test_offset(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]
        self.assertEqual(X.a.offset, 0)
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]
        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.b.offset, ctypes.sizeof(ctypes.c_int))
        class X(ctypes.Structure):
            _pack_ = 1
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_byte),
                        ("c", ctypes.c_int)]
        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.b.offset, ctypes.sizeof(ctypes.c_int))
        self.
