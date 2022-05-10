import ctypes
# Test ctypes.CField

class TestCField(unittest.TestCase):
    def test_field_basic(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]

        self.assertEqual(X._fields_, [("a", ctypes.c_int)])
        self.assertEqual(X._fields_[0][0], "a")
        self.assertEqual(X._fields_[0][1], ctypes.c_int)

        self.assertEqual(X.a, ctypes.c_int)

        self.assertRaises(AttributeError, getattr, X, "b")

    def test_field_duplicate(self):
        with self.assertRaisesRegex(ValueError, "duplicate field"):
            class X(ctypes.Structure):
                _fields_ = [("a", ctypes.c_int), ("a", ctypes.c_int)]

    def test_field_empty(self):
        class X(ctypes.Structure):
           
