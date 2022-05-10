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

        class POINT_PTR(ctypes.Structure):
            _fields_ = [("ptr", ctypes.POINTER(POINT))]

        class RECT_PTR(ctypes.Structure):
            _fields_ = [("ptr", ctypes.POINTER(RECT))]

        class RECT_PTR_PTR(ctypes.Structure):
            _fields_ = [("ptr", ctypes.POINTER(RECT_PTR))]

        self.assertEqual(ctypes.sizeof(POINT), 8)
        self.assertEqual(ctypes.sizeof(RECT), 16)
        self.assertEqual(ctypes.sizeof
