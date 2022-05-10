import ctypes
# Test ctypes.CField
class CFieldTest(unittest.TestCase):
    def test_cfield_init(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]
        self.assertEqual(X._fields_[0][1]._type_, ctypes.c_int)
        self.assertEqual(X._fields_[0][1]._name_, "a")
        self.assertEqual(X._fields_[0][1]._offset_, 0)
        self.assertEqual(X._fields_[0][1]._size_, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(X._fields_[0][1]._index_, 0)
        self.assertEqual(X._fields_[0][1]._pack_, 1)
        self.assertEqual(X._fields_[0][1]._alignment_, ctypes.alignment(ctypes.c_int))
        self.assertEqual(X._fields_[
