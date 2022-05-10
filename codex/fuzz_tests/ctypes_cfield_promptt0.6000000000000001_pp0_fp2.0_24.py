import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_fields(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.c_int)]

        class RECT(ctypes.Structure):
            _fields_ = [("upper_left", POINT),
                        ("lower_right", POINT)]

        self.assertEqual(RECT._fields_,
                         [("upper_left", POINT),
                          ("lower_right", POINT)])
        self.assertEqual(RECT._fields_[0][0], "upper_left")
        self.assertEqual(RECT._fields_[0][1], POINT)
        self.assertEqual(RECT._fields_[1][0], "lower_right")
        self.assertEqual(RECT._fields_[1][1], POINT)

        self.assertEqual(RECT._fields_[0][1]._fields_,
                         [("x", ctypes.c_int),
                
