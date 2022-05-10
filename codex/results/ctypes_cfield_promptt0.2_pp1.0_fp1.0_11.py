import ctypes
# Test ctypes.CField
class CFieldTestCase(unittest.TestCase):
    def test_c_field(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.c_int)]

        class RECT(ctypes.Structure):
            _fields_ = [("ul", POINT),
                        ("lr", POINT)]

        class RECT2(ctypes.Structure):
            _fields_ = [("ul", POINT),
                        ("lr", POINT),
                        ("name", ctypes.c_char * 32)]

        class RECT3(ctypes.Structure):
            _fields_ = [("ul", POINT),
                        ("lr", POINT),
                        ("name", ctypes.c_char * 32),
                        ("dummy", ctypes.c_int)]

        self.assertEqual(ctypes.sizeof(RECT), 8)
        self.assertEqual(ctypes.sizeof(RECT2), 40)
        self.assertEqual(ctypes.
