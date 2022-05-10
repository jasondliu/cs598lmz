import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_cfield(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.c_int)]

        class RECT(ctypes.Structure):
            _fields_ = [("ul", POINT),
                        ("lr", POINT)]

        class RECT2(ctypes.Structure):
            _fields_ = [("ul", POINT),
                        ("lr", POINT),
                        ("width", ctypes.CField)]

        r = RECT()
        r.ul.x = 10
        r.ul.y = 20
        r.lr.x = 30
        r.lr.y = 40
        self.assertEqual(r.width, 20)

        r2 = RECT2()
        r2.ul.x = 10
        r2.ul.y = 20
        r2.lr.x = 30
        r2.lr.y = 40
        self.assertEqual(
