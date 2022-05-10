import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_cfield(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]

        class Y(X):
            _fields_ = [("b", ctypes.c_int)]

        self.assertEqual(X._fields_, [("a", ctypes.c_int)])
        self.assertEqual(Y._fields_, [("b", ctypes.c_int), ("a", ctypes.c_int)])

    def test_cfield_size(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int, 1)]

        class Y(X):
            _fields_ = [("b", ctypes.c_int, 2)]

        self.assertEqual(X._fields_, [("a", ctypes.c_int, 1)])
        self.assertEqual(Y._fields_, [("b", ctypes.c_int, 2),
