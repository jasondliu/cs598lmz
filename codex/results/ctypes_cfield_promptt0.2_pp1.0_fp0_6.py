import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [("x", X),
                ("y", ctypes.c_int)]

class Z(ctypes.Structure):
    _fields_ = [("y", Y),
                ("z", ctypes.c_int)]

class Test(unittest.TestCase):
    def test_field(self):
        self.assertEqual(ctypes.sizeof(X), ctypes.sizeof(ctypes.c_int) * 2)
        self.assertEqual(ctypes.sizeof(Y), ctypes.sizeof(ctypes.c_int) * 3)
        self.assertEqual(ctypes.sizeof(Z), ctypes.sizeof(ctypes.c_int) * 4)

        x = X()
        self.assertEqual(x.a, 0)
        self.assertEqual(x
