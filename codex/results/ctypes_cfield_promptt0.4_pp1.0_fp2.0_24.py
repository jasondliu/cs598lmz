import ctypes
# Test ctypes.CField
class CFieldTest(unittest.TestCase):
    def test_simple(self):
        class X(ctypes.Structure):
            _fields_ = [("f", ctypes.c_int)]
        self.assertEqual(X.f.offset, 0)
        self.assertEqual(X.f.size, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(X.f.name, "f")

    def test_nested(self):
        class Y(ctypes.Structure):
            _fields_ = [("f", ctypes.c_int)]
        class X(ctypes.Structure):
            _fields_ = [("f", Y)]
        self.assertEqual(X.f.offset, 0)
        self.assertEqual(X.f.size, ctypes.sizeof(Y))
        self.assertEqual(X.f.name, "f")

    def test_nested_array(self):
        class Y(ctypes.Structure):
            _fields_ = [
