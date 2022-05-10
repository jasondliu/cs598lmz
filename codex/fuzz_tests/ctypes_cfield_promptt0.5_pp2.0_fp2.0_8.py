import ctypes
# Test ctypes.CField
class CFieldTest(unittest.TestCase):
    def test_simple(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]
        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.a.size, 4)
        self.assertEqual(ctypes.sizeof(X), 4)
        self.assertEqual(X.a.type, ctypes.c_int)
        self.assertEqual(X.a.name, "a")
        self.assertEqual(X.a.pack, 1)
        self.assertEqual(X.a.bitsize, 0)
        self.assertEqual(X.a.index, 0)
        self.assertEqual(X.a.index, 0)
        self.assertEqual(X.a.index, 0)
        self.assertEqual(X.a.index, 0)

    def test_bitfield(self):
        class X(ctypes.Structure):
