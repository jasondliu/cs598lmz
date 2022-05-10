import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_basic(self):
        class X(ctypes.Structure):
            _fields_ = [('a', ctypes.c_int),
                        ('b', ctypes.c_int)]
        self.assertEqual(X.a.offset, ctypes.c_int.size)
        self.assertEqual(X.a.size, ctypes.c_int.size)
        self.assertEqual(X.a.index, 0)
        self.assertEqual(X.a.pack, 1)
        self.assertEqual(X.a.ctype, ctypes.c_int)
        self.assertEqual(X.b.offset, 2 * ctypes.c_int.size)
        self.assertEqual(X.b.size, ctypes.c_int.size)
        self.assertEqual(X.b.index, 1)
        self.assertEqual(X.b.pack, 1)
        self.assertEqual(X.b.ctype
