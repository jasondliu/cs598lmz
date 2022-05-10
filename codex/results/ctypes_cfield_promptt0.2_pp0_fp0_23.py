import ctypes
# Test ctypes.CField
class CFieldTestCase(unittest.TestCase):
    def test_CField_instance(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]
        self.assertEqual(X._fields_[0], ("a", ctypes.c_int))
        self.assertEqual(X._fields_[0][0], "a")
        self.assertEqual(X._fields_[0][1], ctypes.c_int)
        self.assertEqual(X._fields_[0]._type_, ctypes.c_int)
        self.assertEqual(X._fields_[0]._name, "a")
        self.assertEqual(X._fields_[0]._offset, 0)
        self.assertEqual(X._fields_[0]._size, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(X._fields_[0]._length_, None)
        self.assertEqual(X._fields_[0
