import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_simple(self):
        class S(ctypes.Structure):
            _fields_ = [('a', ctypes.c_int)]
        self.assertEqual(S._fields_, [('a', ctypes.c_int)])

    def test_simple_default(self):
        class S(ctypes.Structure):
            _fields_ = [('a', ctypes.c_int, 1)]
        self.assertEqual(S._fields_, [('a', ctypes.c_int, 1)])
        self.assertEqual(S().a, 1)

    def test_simple_default2(self):
        class S(ctypes.Structure):
            _fields_ = [('a', ctypes.c_int, -1)]
        self.assertEqual(S._fields_, [('a', ctypes.c_int, -1)])
        self.assertEqual(S().a, -1)

    def test_simple_default_int(self):
