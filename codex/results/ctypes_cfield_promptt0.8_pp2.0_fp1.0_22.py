import ctypes
# Test ctypes.CField
class CFieldTest(unittest.TestCase):
    def test_get_set_attr(self):
        class S(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.c_char),
                        ("z", ctypes.c_char)]
        #
        self.assertEqual(S.x.offset, 0)
        self.assertEqual(S.y.offset, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(S.z.offset, ctypes.sizeof(ctypes.c_int)+1)
        self.assertEqual(S.x.size, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(S.y.size, 1)
        self.assertEqual(S.z.size, 1)
        self.assertEqual(S.x.index, 0)
        self.assertEqual(S.y.index, 1)
        self.assertEqual(S.z.
