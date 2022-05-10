import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_CField(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.c_int)]

        self.assertEqual(POINT.x.offset, 0)
        self.assertEqual(POINT.y.offset, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(ctypes.sizeof(POINT), 2 * ctypes.sizeof(ctypes.c_int))

        class RECT(ctypes.Structure):
            _fields_ = [("ul", POINT),
                        ("lr", POINT)]

        self.assertEqual(RECT.ul.offset, 0)
        self.assertEqual(RECT.lr.offset, 2 * ctypes.sizeof(ctypes.c_int))
        self.assertEqual(ctypes.sizeof(RECT), 4 * ctypes.sizeof(ctypes.c_int))

        # test that offset
