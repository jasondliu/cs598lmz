import ctypes
# Test ctypes.CField
class CFieldTestCase(unittest.TestCase):
    def test_CField(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.c_int)]

        class RECT(ctypes.Structure):
            _fields_ = [("ul", POINT),
                        ("lr", POINT)]

        r = RECT()
        r.ul.x = 10
        r.ul.y = 20
        r.lr.x = 30
        r.lr.y = 40
        self.assertEqual(r.ul.x, 10)
        self.assertEqual(r.ul.y, 20)
        self.assertEqual(r.lr.x, 30)
        self.assertEqual(r.lr.y, 40)

    def test_CField_in_list(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.
