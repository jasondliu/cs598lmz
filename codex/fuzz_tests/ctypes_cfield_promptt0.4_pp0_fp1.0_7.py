import ctypes
# Test ctypes.CField
class test_CField(unittest.TestCase):
    def test_CField(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]
        self.assertEqual(ctypes.sizeof(X), ctypes.sizeof(ctypes.c_int)*2)
        self.assertEqual(ctypes.sizeof(X), ctypes.sizeof(ctypes.c_long))

        class Y(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int, 16)]
        self.assertEqual(ctypes.sizeof(Y), ctypes.sizeof(ctypes.c_int)*2)

        class Z(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int, 16),
                        ("b", ctypes.c_int)]
        self.assertEqual(ctypes.sizeof(Z), c
