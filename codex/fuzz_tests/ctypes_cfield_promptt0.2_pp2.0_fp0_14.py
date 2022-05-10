import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_CField(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]
        self.assertEqual(X._fields_[0][1], ctypes.CField)
        self.assertEqual(X._fields_[0][1]._type_, ctypes.c_int)
        self.assertEqual(X._fields_[0][1]._name_, "a")
        self.assertEqual(X._fields_[0][1]._offset_, 0)
        self.assertEqual(X._fields_[0][1]._bits_, 0)
        self.assertEqual(X._fields_[0][1]._length_, 0)
        self.assertEqual(X._fields_[0][1]._index_, 0)
        self.assertEqual(X._fields_[0][1]._pack_, 1)
        self.assertEqual(X._fields_[0][
