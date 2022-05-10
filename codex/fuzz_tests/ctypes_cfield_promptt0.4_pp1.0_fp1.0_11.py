import ctypes
# Test ctypes.CField

class CFieldTestCase(unittest.TestCase):
    def test_basic(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]
        self.assertEqual(X.a.offset, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(X.a.size, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(X.a.index, 0)
        self.assertEqual(X.a.pack, 1)
        self.assertEqual(X.a.ctype, ctypes.c_int)
        self.assertEqual(X.a.type, ctypes.c_int)
        self.assertEqual(X.a.bitsize, None)
        self.assertEqual(X.a.flags, 0)
        self.assertEqual(X.a.kind, "field")
        self.assertEqual(X.a.name, "a")
        self.assertEqual(
