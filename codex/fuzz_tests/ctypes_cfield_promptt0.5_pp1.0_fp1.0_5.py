import ctypes
# Test ctypes.CField
class CFieldTest(unittest.TestCase):
    def test_CField(self):
        class X(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]
        self.assertEqual(X._fields_[0][1], ctypes.c_int)
        self.assertEqual(X._fields_[0][0], "a")
        self.assertRaises(TypeError, ctypes.CField, "a", [])
        self.assertRaises(TypeError, ctypes.CField, "a", object)
        self.assertRaises(TypeError, ctypes.CField, "a", "b")
        self.assertRaises(TypeError, ctypes.CField, "a", 2)
        self.assertRaises(TypeError, ctypes.CField, "a", None)
        self.assertRaises(TypeError, ctypes.CField, "a", ctypes.c_int, "b")
        self.assertRaises(TypeError, ctypes.CField, "a",
