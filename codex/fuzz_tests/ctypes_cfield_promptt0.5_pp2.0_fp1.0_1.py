import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_c_field(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_long),
                        ("y", ctypes.c_long)]

        class RECT(ctypes.Structure):
            _fields_ = [("left", ctypes.c_long),
                        ("top", ctypes.c_long),
                        ("right", ctypes.c_long),
                        ("bottom", ctypes.c_long)]

        class POINT_AND_RECT(ctypes.Structure):
            _fields_ = [("pt", POINT),
                        ("rc", RECT)]

        # test the CField type
        class CFIELD(ctypes.Structure):
            _fields_ = [("name", ctypes.c_char * 32),
                        ("value", ctypes.c_long)]

        # test the CField type
        class CFIELD_PTR(ctypes.Structure):
            _fields_ = [("name", ctypes.c_
