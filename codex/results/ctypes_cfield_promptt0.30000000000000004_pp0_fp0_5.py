import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_cfield(self):
        class X(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int)]
        self.assertEqual(X.x.offset, 0)
        self.assertEqual(X.x.size, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(X.x.index, 0)
        self.assertEqual(X.x.pack_, 1)
        self.assertEqual(X.x.bitsize, 32)
        self.assertEqual(X.x.bitoffset, 0)
        self.assertEqual(X.x.type, ctypes.c_int)
        self.assertEqual(X.x.name, "x")
        self.assertEqual(X.x.ctype, ctypes.c_int)
        self.assertEqual(X.x.__doc__, "c_int(x)")
        self.assertEqual(X.x
