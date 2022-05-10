import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_cfield_init(self):
        # Test ctypes.CField.__init__
        class C(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]
        self.assertEqual(C._fields_[0].__class__, ctypes.CField)
        self.assertEqual(C._fields_[0].name, "a")
        self.assertEqual(C._fields_[0].ctype, ctypes.c_int)
        self.assertEqual(C._fields_[0].offset, 0)
        self.assertEqual(C._fields_[0].bitshift, 0)
        self.assertEqual(C._fields_[0].bitsize, 0)
        self.assertEqual(C._fields_[0].flags, 0)
        self.assertEqual(C._fields_[0].index, 0)
        self.assertEqual(C._fields_[0].size, ctypes.sizeof(
