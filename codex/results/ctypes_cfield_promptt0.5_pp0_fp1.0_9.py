import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_CField(self):
        class S(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]
        self.assertEqual(S.a.offset, 0)
        self.assertEqual(S.a.size, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(S.a.index, 0)
        self.assertEqual(S.a.bitsize, ctypes.sizeof(ctypes.c_int) * 8)
        self.assertEqual(S.a.type, ctypes.c_int)
        self.assertEqual(S.a.pack, 1)
        self.assertEqual(S.a.flags, 0)
        self.assertEqual(S.a.name, "a")
        self.assertEqual(S.a.__doc__, "C field a of type c_int")
        self.assertEqual(S.a.__name__, "a")
