import ctypes
# Test ctypes.CField

class TestCField(unittest.TestCase):
    def test_cfield(self):
        class X(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int)]
        self.assertEqual(X.x.offset, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(X.x.size, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(X.x.index, 0)
        self.assertEqual(X.x.pack_, 1)
        self.assertEqual(X.x.bitsize, ctypes.sizeof(ctypes.c_int) * 8)
        self.assertEqual(X.x.flags, 0)
        self.assertEqual(X.x.type, ctypes.c_int)
        self.assertEqual(X.x.name, "x")

    def test_cfield_subclass(self):
        class X(ctypes.Structure):
            _fields_ = [("
