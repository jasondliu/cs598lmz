import ctypes
# Test ctypes.CField
class CFieldTest(unittest.TestCase):
    def test_simple(self):
        class S(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]
        self.assertEqual(S._fields_, [("a", ctypes.c_int)])
        self.assertEqual(S.a.offset, 0)
        self.assertEqual(S.a.size, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(S.a.index, 0)

    def test_simple_2(self):
        class S(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]
        self.assertEqual(S._fields_, [("a", ctypes.c_int),
                                      ("b", ctypes.c_int)])
        self.assertEqual(S.a.offset, 0)
        self.assertEqual(S.a.size, ctypes.
