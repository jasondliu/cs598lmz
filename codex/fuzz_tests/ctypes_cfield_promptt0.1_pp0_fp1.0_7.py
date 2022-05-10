import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_CField(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]
        self.assertEqual(X._fields_[0][1], ctypes.c_int)
        self.assertEqual(X._fields_[0][0], "a")
        self.assertEqual(X._fields_[0][2], 0)
        self.assertEqual(X._fields_[0][3], 0)
        self.assertEqual(X._fields_[0][4], 0)
        self.assertEqual(X._fields_[0][5], 0)
        self.assertEqual(X._fields_[0][6], 0)
        self.assertEqual(X._fields_[0][7], 0)
        self.assertEqual(X._fields_[0][8], 0)
        self.assertEqual(X._fields_[0][9], 0)
        self.assertEqual(X
