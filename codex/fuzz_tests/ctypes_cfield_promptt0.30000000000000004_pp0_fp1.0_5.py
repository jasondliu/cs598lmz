import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_basic(self):
        class C(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]
        self.assertEqual(C.a.offset, 0)
        self.assertEqual(C.b.offset, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(C.a.size, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(C.b.size, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(C.a.index, 0)
        self.assertEqual(C.b.index, 1)
        self.assertEqual(C.a.pack, 1)
        self.assertEqual(C.b.pack, 1)
        self.assertEqual(C.a.bitsize, 32)
        self.assertEqual(C.b.bitsize, 32
