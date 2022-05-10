import ctypes
# Test ctypes.CField

class TestCField(unittest.TestCase):
    def test_cfield(self):
        class C(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int)]
        #
        self.assertRaises(TypeError, ctypes.CField, "x", ctypes.c_int, None)
        #
        x = ctypes.CField("x", ctypes.c_int, None, None)
        self.assertEqual(x.name, "x")
        self.assertEqual(x.type, ctypes.c_int)
        self.assertEqual(x.offset, None)
        self.assertEqual(x.func, None)
        #
        x = ctypes.CField("x", ctypes.c_int, 0, None)
        self.assertEqual(x.offset, 0)
        #
        x = ctypes.CField("x", ctypes.c_int, 0, lambda self: None)
        self.assertEqual(x.func, lambda self:
