import ctypes
# Test ctypes.CField
class CFieldTestCase(unittest.TestCase):
    def test_cfield(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.c_int)]

        class RECT(ctypes.Structure):
            _fields_ = [("ul", POINT),
                        ("lr", POINT)]

        class RECT_ARRAY(ctypes.Structure):
            _fields_ = [("rects", ctypes.c_int * 4),
                        ("rect_array", RECT * 4)]

        class RECT_ARRAY_ARRAY(ctypes.Structure):
            _fields_ = [("rect_array_array", RECT_ARRAY * 4)]

        class RECT_ARRAY_ARRAY_ARRAY(ctypes.Structure):
            _fields_ = [("rect_array_array_array", RECT_ARRAY_ARRAY * 4)]

        class RECT_ARRAY_ARRAY_ARRAY_ARRAY(ctypes.Structure
