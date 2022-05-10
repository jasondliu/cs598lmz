import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_basic(self):
        class X(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int, 1)]
        self.assertEqual(X.x.offset, 0)
        self.assertEqual(X.x.size, 4)
        self.assertEqual(X.x.bitsize, 1)
        self.assertEqual(X.x.bitoffset, 0)
        self.assertEqual(X.x.type, ctypes.c_int)
        self.assertEqual(X.x.index, 0)
        self.assertEqual(X.x.pack, 1)

        class X(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int, 1),
                        ("y", ctypes.c_int, 1)]
        self.assertEqual(X.x.offset, 0)
        self.assertEqual(X.x.size, 8)
        self.assertEqual(X
