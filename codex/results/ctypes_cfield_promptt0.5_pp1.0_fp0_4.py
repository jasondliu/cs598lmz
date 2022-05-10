import ctypes
# Test ctypes.CField

class TestField(unittest.TestCase):

    def test_field(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int, 2)]
        self.assertEqual(ctypes.sizeof(X), 8)
        self.assertEqual(ctypes.alignment(X), 4)
        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.b.offset, 4)
        self.assertEqual(X.a.size, 4)
        self.assertEqual(X.b.size, 2)
        self.assertEqual(X.a.bitsize, 32)
        self.assertEqual(X.b.bitsize, 2)
        self.assertEqual(X.a.bitoffset, 0)
        self.assertEqual(X.b.bitoffset, 32)
        self.assertEqual(X.a.type, ctypes.c_int)
        self
