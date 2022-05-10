import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_CField(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_long),
                        ("y", ctypes.c_long)]
        class RECT(ctypes.Structure):
            _fields_ = [("a", POINT),
                        ("b", POINT)]
        self.assertEqual(RECT._fields_, [("a", POINT),
                                         ("b", POINT)])
        self.assertEqual(RECT.a._fields_, [("x", ctypes.c_long),
                                           ("y", ctypes.c_long)])
        self.assertEqual(RECT.b._fields_, [("x", ctypes.c_long),
                                           ("y", ctypes.c_long)])
        self.assertEqual(RECT.a.x.offset, 0)
        self.assertEqual(RECT.a.y.offset, ctypes.sizeof(ctypes.c_long))
