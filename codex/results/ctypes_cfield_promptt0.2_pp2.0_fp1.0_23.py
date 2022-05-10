import ctypes
# Test ctypes.CField
class CFieldTestCase(unittest.TestCase):
    def test_CField(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]
        self.assertEqual(X._fields_, [("a", ctypes.c_int),
                                      ("b", ctypes.c_int)])
        self.assertEqual(X._pack_, 1)
        self.assertEqual(X._anonymous_, [])
        self.assertEqual(X._abstract_, False)
        self.assertEqual(X._is_union_, False)
        self.assertEqual(X._align_, ctypes.c_int._align_)
        self.assertEqual(X._length_, 2)
        self.assertEqual(X._subclasses_, [])
        self.assertEqual(X._name_, "X")
        self.assertEqual(X._as_parameter_, None)
       
