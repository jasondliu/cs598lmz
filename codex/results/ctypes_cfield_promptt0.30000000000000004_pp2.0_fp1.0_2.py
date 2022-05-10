import ctypes
# Test ctypes.CField

class TestCF(unittest.TestCase):
    def test_field(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]

        self.assertEqual(X._fields_, [("a", ctypes.c_int)])
        self.assertEqual(X._pack_, 1)
        self.assertEqual(X.a.offset, 0)
        self.assertEqual(X.a.size, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(X.a.index, 0)
        self.assertEqual(X.a.pack, 1)

    def test_field_2(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]
        self.assertEqual(X._fields_, [("a", ctypes.c_int),
                                      ("b", ctypes.c_int)])
       
