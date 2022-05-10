import ctypes
# Test ctypes.CField
class CFieldTestCase(unittest.TestCase):
    def test_cfield(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.c_int)]

        class RECT(ctypes.Structure):
            _fields_ = [("upperleft", POINT),
                        ("lowerright", POINT)]

        class RECT2(ctypes.Structure):
            _fields_ = [("upperleft", POINT),
                        ("lowerright", POINT)]

        class RECT3(ctypes.Structure):
            _fields_ = [("upperleft", POINT),
                        ("lowerright", POINT)]

        class RECT4(ctypes.Structure):
            _fields_ = [("upperleft", POINT),
                        ("lowerright", POINT)]

        class RECT5(ctypes.Structure):
            _fields_ = [("upperleft", POINT),
                        ("lowerright", POINT)]

        class RECT6(ctypes.Structure
