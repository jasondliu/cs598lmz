import ctypes
# Test ctypes.CField
class CFieldTest(unittest.TestCase):
    def test_simple(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]
        self.assertEqual(X._fields_, [("a", ctypes.c_int)])
        self.assertEqual(X._pack_, 1)
        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.a.size, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(X.a.index, 0)
        self.assertEqual(X.a.pack, 1)
        self.assertEqual(X.a.bitsize, 32)
        self.assertEqual(X.a.type, ctypes.c_int)
        self.assertEqual(X.a.name, "a")
        self.assertEqual(X.a.ctype, ctypes.c_int)
        self.assertEqual(X.a.from_
