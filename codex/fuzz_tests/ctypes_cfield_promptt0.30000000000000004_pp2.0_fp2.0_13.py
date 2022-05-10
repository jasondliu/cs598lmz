import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_cfield(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]
        self.assertEqual(X._fields_[0][1], ctypes.c_int)
        self.assertEqual(X._fields_[0][0], "a")

        self.assertEqual(X._fields_[0][1]._type_, "i")
        self.assertEqual(X._fields_[0][1]._length_, 1)

        self.assertEqual(X._fields_[0][1]._type_, "i")
        self.assertEqual(X._fields_[0][1]._length_, 1)

        class Y(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]
        self.assertEqual(Y._fields_[0][1], ctypes.c_int)
        self
