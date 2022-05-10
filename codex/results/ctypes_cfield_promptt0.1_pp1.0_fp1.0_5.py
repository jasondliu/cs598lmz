import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_CField(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.c_int)]

        class RECT(ctypes.Structure):
            _fields_ = [("ul", POINT),
                        ("lr", POINT)]

        class RECT2(ctypes.Structure):
            _fields_ = [("ul", POINT),
                        ("lr", POINT),
                        ("name", ctypes.c_char_p)]

        class RECT3(ctypes.Structure):
            _fields_ = [("ul", POINT),
                        ("lr", POINT),
                        ("name", ctypes.c_char_p),
                        ("name2", ctypes.c_char_p)]

        class RECT4(ctypes.Structure):
            _fields_ = [("ul", POINT),
                        ("lr", POINT),
                        ("name", ctypes.c_char_p),
