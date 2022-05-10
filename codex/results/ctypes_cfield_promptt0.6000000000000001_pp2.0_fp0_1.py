import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_CField(self):
        # This test is really just documentation.
        class POINT(ctypes.Structure):
            _fields_ = [('x', ctypes.c_int),
                        ('y', ctypes.c_int)]

        class RECT(ctypes.Structure):
            _fields_ = [('a', POINT),
                        ('b', POINT)]

        class MyUnion(ctypes.Union):
            _fields_ = [('rect', RECT),
                        ('points', POINT * 2)]

        class MyStruct(ctypes.Structure):
            _fields_ = [('rect', RECT),
                        ('union', MyUnion)]

        self.assertEqual(MyUnion.points[1].x.offset,
                             ctypes.sizeof(POINT) + ctypes.sizeof(POINT.x))
        self.assertEqual(MyUnion.points[1].x.offset,
                             MyUnion.points[1].y.offset - ctypes.sizeof(
