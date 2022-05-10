import ctypes
# Test ctypes.CField
class CFieldTest(unittest.TestCase):
    def test_simple(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]
        self.assertEqual(X._fields_, [("a", ctypes.c_int)])
        self.assertEqual(X._pack_, 1)
        self.assertEqual(X._anonymous_, [])
        self.assertEqual(X._abstract_, False)
        self.assertEqual(X._align_, ctypes.c_int._align_)
        self.assertEqual(X._length_, 1)
        self.assertEqual(X._subclasshook_, None)
        self.assertEqual(X._is_packed_, False)
        self.assertEqual(X._needs_hash_, True)
        self.assertEqual(X._needs_eq_, True)
        self.assertEqual(X._needs_cmp_, True)
        self.assertEqual(X._needs
