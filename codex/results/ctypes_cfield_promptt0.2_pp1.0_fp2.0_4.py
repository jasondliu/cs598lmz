import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_CField(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.c_int)]

        class RECT(ctypes.Structure):
            _fields_ = [("ul", POINT),
                        ("lr", POINT)]

        class RECT_ARRAY(ctypes.Structure):
            _fields_ = [("rects", ctypes.CField("nrects", RECT))]

        ra = RECT_ARRAY()
        self.assertEqual(ra.rects, None)
        self.assertEqual(ra._objects, None)

        ra.nrects = 3
        self.assertEqual(len(ra.rects), 3)
        self.assertEqual(len(ra._objects), 3)

        ra.rects[0].ul.x = 1
        ra.rects[0].ul.y = 2
        ra.rects[0].lr
