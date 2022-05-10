import ctypes
# Test ctypes.CField
class CFieldTest(unittest.TestCase):
    def test_CField(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.c_int)]

        class RECT(ctypes.Structure):
            _fields_ = [("ul", POINT),
                        ("lr", POINT)]

        r = RECT()
        self.assertEqual(r.ul.x, 0)
        self.assertEqual(r.ul.y, 0)
        self.assertEqual(r.lr.x, 0)
        self.assertEqual(r.lr.y, 0)

        r.ul.x = 10
        r.ul.y = 20
        r.lr.x = 30
        r.lr.y = 40

        self.assertEqual(r.ul.x, 10)
        self.assertEqual(r.ul.y, 20)
        self.assertEqual(r.lr.x, 30)
        self.
