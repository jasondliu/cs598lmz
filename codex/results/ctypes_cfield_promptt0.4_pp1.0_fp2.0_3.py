import ctypes
# Test ctypes.CField

class CFieldTestCase(unittest.TestCase):
    def test_constructor(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]
        x = X()
        self.assertEqual(x.a, 0)
        self.assertEqual(x._fields_, [("a", ctypes.c_int)])

        class Y(X):
            pass
        y = Y()
        self.assertEqual(y.a, 0)
        self.assertEqual(y._fields_, [("a", ctypes.c_int)])

        class Z(X):
            _fields_ = [("b", ctypes.c_int)]
        z = Z()
        self.assertEqual(z.a, 0)
        self.assertEqual(z._fields_, [("b", ctypes.c_int)])

        class W(X):
            _fields_ = [("b", ctypes.c_int), ("a", ctypes.c_int)]
