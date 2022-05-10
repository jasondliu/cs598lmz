import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_CField(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.c_int)]

        class RECT(ctypes.Structure):
            _fields_ = [("a", POINT),
                        ("b", POINT)]

        r = RECT()
        r.a.x = 10
        r.a.y = 20
        r.b.x = 30
        r.b.y = 40
        self.assertEqual(r.a.x, 10)
        self.assertEqual(r.a.y, 20)
        self.assertEqual(r.b.x, 30)
        self.assertEqual(r.b.y, 40)

    def test_CField_2(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.c_int
