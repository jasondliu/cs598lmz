import ctypes
# Test ctypes.CField.
import ctypes.test.test_cf

class CFieldTestCase(unittest.TestCase):
    def test_simple(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]
        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.a.size, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(X.a.index, 0)
        self.assertEqual(X.a.pack, 1)
        self.assertEqual(X.a.bitsize, ctypes.sizeof(ctypes.c_int) * 8)
        self.assertEqual(X.a.bitoffset, 0)

    def test_simple_2(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]
        self.assertEqual(X.a.offset, 0)
        self
