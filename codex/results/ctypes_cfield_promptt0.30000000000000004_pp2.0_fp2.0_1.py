import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_CField(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.CField)]
        self.assertEqual(X._fields_[0][1], ctypes.CField)
        self.assertEqual(X._fields_[0][0], "a")
        self.assertEqual(X._fields_[0][2], 0)
        self.assertEqual(X._fields_[0][3], None)
        self.assertEqual(X._fields_[0][4], None)
        self.assertEqual(X._fields_[0][5], None)
        self.assertEqual(X._fields_[0][6], None)
        self.assertEqual(X._fields_[0][7], None)
        self.assertEqual(X._fields_[0][8], None)
        self.assertEqual(X._fields_[0][9], None)
        self.assertEqual(X._fields
