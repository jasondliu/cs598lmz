import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_CField(self):
        class C(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]
        self.assertEqual(C._fields_[0][1]._type_, "i")
        self.assertEqual(C._fields_[0][1]._length_, 1)
        self.assertEqual(C._fields_[0][1]._is_array_, False)
        self.assertEqual(C._fields_[0][1]._is_pointer_, False)
        self.assertEqual(C._fields_[0][1]._is_void_pointer_, False)
        self.assertEqual(C._fields_[0][1]._is_simple_, True)
        self.assertEqual(C._fields_[0][1]._is_pointer_to_simple_, False)
        self.assertEqual(C._fields_[0][1]._is_struct_, False)
       
