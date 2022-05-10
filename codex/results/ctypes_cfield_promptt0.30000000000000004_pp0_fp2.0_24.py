import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_cfield(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]

        class RECT(ctypes.Structure):
            _fields_ = [("upperleft", POINT), ("lowerright", POINT)]

        class POINT_PTR(ctypes.Structure):
            _fields_ = [("ptr", ctypes.POINTER(POINT))]

        class RECT_PTR(ctypes.Structure):
            _fields_ = [("ptr", ctypes.POINTER(RECT))]

        class POINT_PTR_PTR(ctypes.Structure):
            _fields_ = [("ptr", ctypes.POINTER(POINT_PTR))]

        class RECT_PTR_PTR(ctypes.Structure):
            _fields_ = [("ptr", ctypes.POINTER(RECT_PTR))]

        # Test POINTER(POINTER(PO
