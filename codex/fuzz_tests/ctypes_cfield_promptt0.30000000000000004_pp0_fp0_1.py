import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_CField(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.c_int)]

        class RECT(ctypes.Structure):
            _fields_ = [("upper_left", POINT),
                        ("lower_right", POINT)]

        r = RECT()
        r.upper_left.x = 1
        r.upper_left.y = 2
        r.lower_right.x = 3
        r.lower_right.y = 4
        self.assertEqual(r.upper_left.x, 1)
        self.assertEqual(r.upper_left.y, 2)
        self.assertEqual(r.lower_right.x, 3)
        self.assertEqual(r.lower_right.y, 4)

    def test_CField_instance(self):
        class POINT(ctypes.Structure):
            _fields_ = [("
