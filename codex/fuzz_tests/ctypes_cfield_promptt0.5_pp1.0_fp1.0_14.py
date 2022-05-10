import ctypes
# Test ctypes.CField

class TestCField(unittest.TestCase):
    def test_cfield_simple(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_long),
                        ("y", ctypes.c_long)]

        class RECT(ctypes.Structure):
            _fields_ = [("ul", POINT),
                        ("lr", POINT)]

        class COMPLEX(ctypes.Structure):
            _fields_ = [("real", ctypes.c_double),
                        ("imag", ctypes.c_double)]

        class POLY(ctypes.Structure):
            _fields_ = [("shape", ctypes.c_char),
                        ("points", RECT),
                        ("color", ctypes.c_int),
                        ("complex", COMPLEX)]

        p = POLY(b"Q", RECT(POINT(1, 2), POINT(3, 4)), 5, COMPLEX(6.0, 7.0))
        self.assertEqual(p.shape, b"Q")

