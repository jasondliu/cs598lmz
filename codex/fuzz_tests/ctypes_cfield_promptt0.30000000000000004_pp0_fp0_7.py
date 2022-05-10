import ctypes
# Test ctypes.CField
class CFieldTestCase(unittest.TestCase):
    def test_simple(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]
        self.assertEqual(X._fields_[0][1], ctypes.c_int)

    def test_simple_subclass(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]
        class Y(X):
            _fields_ = [("b", ctypes.c_int)]
        self.assertEqual(Y._fields_[0][1], ctypes.c_int)
        self.assertEqual(Y._fields_[1][1], ctypes.c_int)

    def test_simple_subclass_override(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]
        class Y(X):
            _fields_ = [("a", ctypes.c_int)]
       
