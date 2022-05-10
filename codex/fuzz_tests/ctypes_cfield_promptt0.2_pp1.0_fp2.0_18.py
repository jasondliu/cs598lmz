import ctypes
# Test ctypes.CField
class CFieldTestCase(unittest.TestCase):
    def test_CField(self):
        class C(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]
        self.assertEqual(C._fields_, [("a", ctypes.c_int),
                                      ("b", ctypes.c_int)])
        self.assertEqual(C._pack_, 1)
        self.assertEqual(C._anonymous_, [])
        self.assertEqual(C._abstract_, False)
        self.assertEqual(C._is_union_, False)
        self.assertEqual(C._align_, ctypes.c_int._align_)
        self.assertEqual(C.a, ctypes.c_int)
        self.assertEqual(C.b, ctypes.c_int)
        self.assertEqual(C.a.offset, 0)
        self.assertEqual(C.b.offset
