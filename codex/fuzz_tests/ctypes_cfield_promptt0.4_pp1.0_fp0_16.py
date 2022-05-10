import ctypes
# Test ctypes.CField

class TestCField(unittest.TestCase):
    def test_simple(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]
        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.a.size, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(X.a.index, 0)
        self.assertEqual(X.a.pack, 0)
        self.assertEqual(X.a.type, ctypes.c_int)

    def test_simple_pack(self):
        class X(ctypes.Structure):
            _pack_ = 1
            _fields_ = [("a", ctypes.c_int)]
        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.a.size, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(X.a.index, 0)
        self.
