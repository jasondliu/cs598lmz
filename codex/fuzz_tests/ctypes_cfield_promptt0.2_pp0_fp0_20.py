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

        class RECT2(ctypes.Structure):
            _fields_ = [("ul", POINT),
                        ("lr", POINT),
                        ("area", ctypes.c_int)]

        rect = RECT((1, 2), (3, 4))
        self.assertEqual(rect.ul.x, 1)
        self.assertEqual(rect.ul.y, 2)
        self.assertEqual(rect.lr.x, 3)
        self.assertEqual(rect.lr.y, 4)
        self.assertEqual(ctypes.sizeof(rect), ctypes.sizeof(RECT2))

        rect2 = RECT2
