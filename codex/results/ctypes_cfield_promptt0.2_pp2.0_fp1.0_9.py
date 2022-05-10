import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_cfield(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]
        self.assertEqual(ctypes.sizeof(X), 8)
        self.assertEqual(ctypes.alignment(X), 4)
        self.assertEqual(X._fields_, [("a", ctypes.c_int),
                                      ("b", ctypes.c_int)])
        self.assertEqual(X._pack_, 4)
        self.assertEqual(X._anonymous_, [])
        self.assertEqual(X._abstract_, False)
        self.assertEqual(X._is_union_, False)
        self.assertEqual(X._objects, {})

        self.assertEqual(X._fields_[0][0], "a")
        self.assertEqual(X._fields_[0][1], ctypes.c
