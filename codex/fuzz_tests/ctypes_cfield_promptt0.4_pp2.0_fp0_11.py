import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_cfield(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]
        self.assertEqual(X._fields_, [("a", ctypes.c_int)])
        self.assertRaises(TypeError, ctypes.CField, "a", ctypes.c_int)
        self.assertRaises(TypeError, ctypes.CField, "a", ctypes.c_int, 1)
        self.assertRaises(TypeError, ctypes.CField, "a", ctypes.c_int, 1, 2)
        self.assertRaises(TypeError, ctypes.CField, "a", ctypes.c_int, 1, 2, 3)
        self.assertRaises(TypeError, ctypes.CField, "a", ctypes.c_int, 1, 2, 3, 4)
        self.assertRaises(TypeError, ctypes.CField, "a", ctypes.c_
