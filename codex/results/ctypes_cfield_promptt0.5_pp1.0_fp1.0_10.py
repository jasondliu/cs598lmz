import ctypes
# Test ctypes.CField

class TestCField(unittest.TestCase):
    def test_cfield(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]
        self.assertEqual(X._fields_[0][1].__class__, ctypes._CField)
        self.assertEqual(X._fields_[0][1].type, ctypes.c_int)
        self.assertEqual(X._fields_[0][1].offset, 0)
        self.assertEqual(X._fields_[0][1].size, ctypes.sizeof(ctypes.c_int))

    def test_cfield_with_offset(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int, 1)]
        self.assertEqual(X._fields_[0][1].__class__, ctypes._CField)
        self.assertEqual(X._fields_[0][1].type, ctypes.c_int)

