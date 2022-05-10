import ctypes
# Test ctypes.CField

class CFieldTestCase(unittest.TestCase):
    def test_simple(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]
        self.assertEqual(X._fields_, [("a", ctypes.c_int)])
        self.assertEqual(X._pack_, 1)
        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.a.size, ctypes.sizeof(ctypes.c_int))

    def test_simple_pack(self):
        class X(ctypes.Structure):
            _pack_ = 2
            _fields_ = [("a", ctypes.c_int)]
        self.assertEqual(X._fields_, [("a", ctypes.c_int)])
        self.assertEqual(X._pack_, 2)
        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.a.size, ctypes.sizeof
