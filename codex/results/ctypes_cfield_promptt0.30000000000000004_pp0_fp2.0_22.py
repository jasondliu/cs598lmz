import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_cfield(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_long),
                        ("y", ctypes.c_long)]

        class RECT(ctypes.Structure):
            _fields_ = [("ul", POINT),
                        ("lr", POINT)]

        class RECT_ARRAY(ctypes.Structure):
            _fields_ = [("rects", ctypes.c_long * 2),
                        ("array", RECT * 2)]

        r = RECT_ARRAY()
        self.assertEqual(r.rects[0], 0)
        self.assertEqual(r.rects[1], 0)
        self.assertEqual(r.array[0].ul.x, 0)
        self.assertEqual(r.array[0].ul.y, 0)
        self.assertEqual(r.array[0].lr.x, 0)
        self.assertEqual(r.
