import ctypes
# Test ctypes.CField
class CFieldTestCase(unittest.TestCase):
    def test_cfield(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]
        class Y(ctypes.Structure):
            _fields_ = [("x", X),
                        ("y", ctypes.c_int)]

        self.assertEqual(ctypes.sizeof(X), ctypes.sizeof(ctypes.c_int) * 2)
        self.assertEqual(ctypes.sizeof(Y), ctypes.sizeof(ctypes.c_int) * 3)

        y = Y()
        self.assertEqual(y.x.a, 0)
        self.assertEqual(y.x.b, 0)
        self.assertEqual(y.y, 0)

        y.x.a = 42
        y.x.b = 24
        y.y = 100

        self.assertEqual(y.x.a, 42)
