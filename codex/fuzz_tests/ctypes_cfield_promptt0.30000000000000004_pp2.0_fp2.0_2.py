import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_CField(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]
        self.assertEqual(X._fields_[0][1]._type_, "i")
        self.assertEqual(X._fields_[0][1]._length_, 1)
        self.assertEqual(X._fields_[0][1]._is_array_, False)
        self.assertEqual(X._fields_[0][1]._is_pointer_, False)
        self.assertEqual(X._fields_[0][1]._is_simple_, True)
        self.assertEqual(X._fields_[0][1]._is_bitfield_, False)
        self.assertEqual(X._fields_[0][1]._is_union_, False)
        self.assertEqual(X._fields_[0][1]._is_struct_, False)
        self.assertEqual
