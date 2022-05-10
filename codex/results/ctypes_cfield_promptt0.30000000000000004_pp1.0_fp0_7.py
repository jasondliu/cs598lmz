import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_cfield(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.c_int)]

        class RECT(ctypes.Structure):
            _fields_ = [("upperleft", POINT),
                        ("lowerright", POINT)]

        class RECT_ARRAY(ctypes.Structure):
            _fields_ = [("rects", RECT * 3)]

        class RECT_ARRAY_ARRAY(ctypes.Structure):
            _fields_ = [("rectarrays", RECT_ARRAY * 2)]

        class RECT_ARRAY_ARRAY_ARRAY(ctypes.Structure):
            _fields_ = [("rectarrayarrays", RECT_ARRAY_ARRAY * 2)]

        # Test ctypes.CField
        self.assertEqual(ctypes.CField.from_address(id(RECT.upperleft), RECT).offset, ctypes.size
