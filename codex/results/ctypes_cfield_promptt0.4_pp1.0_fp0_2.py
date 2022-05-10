import ctypes
# Test ctypes.CField
class CFieldTestCase(unittest.TestCase):
    def test_cfield(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int),
                        ("c", ctypes.c_int),
                        ("d", ctypes.c_int),
                        ("e", ctypes.c_int),
                        ("f", ctypes.c_int),
                        ("g", ctypes.c_int),
                        ("h", ctypes.c_int)]
        self.assertEqual(ctypes.sizeof(X), 32)
        self.assertEqual(ctypes.sizeof(X._fields_[0][0]), 4)
        self.assertEqual(ctypes.sizeof(X._fields_[1][0]), 4)
        self.assertEqual(ctypes.sizeof(X._fields_[2][0]), 4)
        self.assertEqual(ctypes.sizeof(X._fields_[3][0]), 4)
       
