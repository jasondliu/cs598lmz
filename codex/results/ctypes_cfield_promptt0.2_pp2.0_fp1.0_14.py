import ctypes
# Test ctypes.CField
class CFieldTestCase(unittest.TestCase):
    def test_cfield(self):
        class C(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]
        self.assertEqual(C._fields_, [("a", ctypes.c_int), ("b", ctypes.c_int)])
        self.assertEqual(C._pack_, 1)
        self.assertEqual(C._anonymous_, [])
        self.assertEqual(C._abstract_, False)
        self.assertEqual(C._is_packed_, False)
        self.assertEqual(C._alignment_, ctypes.c_int.alignment)
        self.assertEqual(C._length_, 2)
        self.assertEqual(C._subclasses_, [])
        self.assertEqual(C._name_, "C")
        self.assertEqual(C._as_parameter_, None)
        self.
