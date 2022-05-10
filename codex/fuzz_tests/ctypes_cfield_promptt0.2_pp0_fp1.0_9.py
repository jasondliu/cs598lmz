import ctypes
# Test ctypes.CField
class CFieldTestCase(unittest.TestCase):
    def test_cfield_init(self):
        # Test ctypes.CField.__init__()
        class C(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]
        self.assertEqual(C._fields_[0][1]._type_, ctypes.c_int)
        self.assertEqual(C._fields_[0][1]._name_, "a")
        self.assertEqual(C._fields_[0][1]._offset_, 0)
        self.assertEqual(C._fields_[0][1]._size_, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(C._fields_[0][1]._index_, 0)
        self.assertEqual(C._fields_[0][1]._pack_, 1)
        self.assertEqual(C._fields_[0][1]._alignment_, ctypes.alignment(ctypes.c_
