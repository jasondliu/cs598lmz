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
        r.ul.x = 1
        r.ul.y = 2
        r.lr.x = 3
        r.lr.y = 4
        self.assertEqual(r.ul.x, 1)
        self.assertEqual(r.ul.y, 2)
        self.assertEqual(r.lr.x, 3)
        self.assertEqual(r.lr.y, 4)
        self.assertEqual(r.ul.x, 1)
        self.assertEqual(r.ul.y, 2)
        self.assertEqual(r.lr.x, 3)
        self.
