import ctypes
# Test ctypes.CField
class CFieldTestCase(unittest.TestCase):
    def test_CField_instance(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.c_int)]
        self.assertEqual(POINT.x.__class__, ctypes.CField)
        self.assertEqual(POINT.y.__class__, ctypes.CField)

    def test_CField_name(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.c_int)]
        self.assertEqual(POINT.x.name, "x")
        self.assertEqual(POINT.y.name, "y")

    def test_CField_offset(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.c_int)]

