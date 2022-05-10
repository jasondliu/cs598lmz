import ctypes
# Test ctypes.CField
class CFieldTest(unittest.TestCase):
    def test_cfield(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.c_int)]

        class RECT(ctypes.Structure):
            _fields_ = [("ul", POINT),
                        ("lr", POINT)]

        class RECT_ARRAY(ctypes.Structure):
            _fields_ = [("rects", RECT * 2)]

        class RECT_PTR(ctypes.Structure):
            _fields_ = [("rects", ctypes.POINTER(RECT))]

        class RECT_PTR_ARRAY(ctypes.Structure):
            _fields_ = [("rects", ctypes.POINTER(RECT) * 2)]

        class RECT_PTR_ARRAY_ARRAY(ctypes.Structure):
            _fields_ = [("rects", ctypes.POINTER(RECT_PTR_ARRAY))]

        class RECT_
