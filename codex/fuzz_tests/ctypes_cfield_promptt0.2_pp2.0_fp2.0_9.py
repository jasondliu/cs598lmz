import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_cfield(self):
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_long),
                        ("y", ctypes.c_long)]
        self.assertEqual(POINT.x.offset, 0)
        self.assertEqual(POINT.y.offset, ctypes.sizeof(ctypes.c_long))
        self.assertEqual(POINT.x.size, ctypes.sizeof(ctypes.c_long))
        self.assertEqual(POINT.y.size, ctypes.sizeof(ctypes.c_long))
        self.assertEqual(POINT.x.index, 0)
        self.assertEqual(POINT.y.index, 1)
        self.assertEqual(POINT.x.pack, 1)
        self.assertEqual(POINT.y.pack, 1)
        self.assertEqual(POINT.x.type, ctypes.c_long)

