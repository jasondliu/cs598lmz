import ctypes
# Test ctypes.CField
class CFieldTestCase(unittest.TestCase):
    def test_CField(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_long),
                        ("y", ctypes.c_long)]

        class RECT(ctypes.Structure):
            _fields_ = [("a", ctypes.c_long),
                        ("b", ctypes.c_long),
                        ("c", ctypes.c_long),
                        ("d", ctypes.c_long)]

        class MyUnion(ctypes.Union):
            _fields_ = [("pt", POINT),
                        ("rc", RECT)]

        u = MyUnion()
        u.pt.x = 11
        u.pt.y = 22
        self.assertEqual(u.pt.x, 11)
        self.assertEqual(u.pt.y, 22)
        self.assertEqual(u.rc.a, 11)
        self.assertEqual(u.rc.b, 22)
        self.assert
