import ctypes
# Test ctypes.CField.
class _TestCField(object):
    def __init__(self):
        self.x = ctypes.c_int(0)
        self.y = ctypes.c_int(0)
        self.z = ctypes.c_int(0)
        self.w = ctypes.c_int(0)
        self.name = "name"
        self.s = "s"

class TestCField(unittest.TestCase):
    def test_cfield1(self):
        tc = _TestCField()
        self.assertEqual(tc.x, 0)
        self.assertEqual(tc.y, 0)
        self.assertEqual(tc.z, 0)

    def test_cfield2(self):
        tc = _TestCField()
        self.assertEqual(tc.w, 0)
        tc.w = 42
        self.assertEqual(tc.w, 42)
        self.assertEqual(tc.z, 0)

    def test_cfield3(self):
        tc
