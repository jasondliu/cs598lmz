import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_fields(self):
        class POINT(ctypes.Structure):
            _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

        class RECT(ctypes.Structure):
            _fields_ = [('upper_left', POINT), ('lower_right', POINT)]

        self.assertEqual(ctypes.sizeof(RECT), 2 * ctypes.sizeof(POINT))
        self.assertEqual(ctypes.sizeof(RECT.upper_left), ctypes.sizeof(POINT))
        self.assertEqual(ctypes.sizeof(RECT.lower_right), ctypes.sizeof(POINT))

    def test_anonymous_fields(self):
        class POINT(ctypes.Structure):
            _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

        class RECT(ctypes.Structure):
            _fields_ = [('upper_left',
