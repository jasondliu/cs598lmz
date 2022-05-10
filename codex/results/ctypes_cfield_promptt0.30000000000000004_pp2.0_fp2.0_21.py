import ctypes
# Test ctypes.CField
class CFieldTest(unittest.TestCase):
    def test_CField(self):
        class S(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]
        self.assertEqual(S.a.offset, 0)
        self.assertEqual(S.b.offset, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(S.a.size, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(S.b.size, ctypes.sizeof(ctypes.c_int))

        class S(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_char)]
        self.assertEqual(S.a.offset, 0)
        self.assertEqual(S.b.offset, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(S.a.size
