import ctypes
# Test ctypes.CField
class CFieldTest(unittest.TestCase):
    def test_simple(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]
        self.assertEqual(X._fields_, [("a", ctypes.c_int)])
        self.assertEqual(X.a, ctypes.c_int)
        self.assertEqual(X.a._type_, "i")
        self.assertEqual(X.a._name, "a")
        self.assertEqual(X.a._offset_, 0)
        self.assertEqual(X.a._index, 0)
        self.assertEqual(X.a._ctype, ctypes.c_int)

    def test_simple_2(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]
        self.assertEqual(X._fields_, [("a", ctypes.c
