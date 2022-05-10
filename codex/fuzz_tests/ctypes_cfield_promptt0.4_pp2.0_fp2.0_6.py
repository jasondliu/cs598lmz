import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_CField(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]
        self.assertEqual(X._fields_[0][1].__class__, ctypes.CField)
        self.assertEqual(X._fields_[0][1]._type_, ctypes.c_int)
    def test_getattr(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]
        x = X()
        self.assertEqual(x.a, 0)
        x.a = 42
        self.assertEqual(x.a, 42)
    def test_setattr(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]
        x = X()
        x.a = 42
        self.assertEqual(x.a, 42)
        x.a =
