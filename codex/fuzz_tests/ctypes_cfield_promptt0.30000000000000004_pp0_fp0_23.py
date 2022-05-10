import ctypes
# Test ctypes.CField
class CFieldTest(unittest.TestCase):
    def test_cfield_init(self):
        class C(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]
        self.assertEqual(C._fields_[0][1]._type_, "i")
        self.assertEqual(C._fields_[0][1]._name_, "a")
        self.assertEqual(C._fields_[0][1]._offset_, 0)
        self.assertEqual(C._fields_[0][1]._size_, 4)
        self.assertEqual(C._fields_[0][1]._index_, 0)
        self.assertEqual(C._fields_[0][1]._pack_, 1)
        self.assertEqual(C._fields_[0][1]._alignment_, 4)
        self.assertEqual(C._fields_[0][1]._is_packed_, False)
        self.assertEqual(C._fields_[0
