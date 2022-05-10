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

        r = RECT()
        self.assertEqual(0, r.ul.x)
        self.assertEqual(0, r.ul.y)
        self.assertEqual(0, r.lr.x)
        self.assertEqual(0, r.lr.y)

        r.ul.x = 10
        r.ul.y = 20
        r.lr.x = 30
        r.lr.y = 40

        self.assertEqual(10, r.ul.x)
        self.assertEqual(20, r.ul.y)
        self.assertEqual(30, r.lr.x)
        self
