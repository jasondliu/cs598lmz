import ctypes
# Test ctypes.CField
class CFieldTest(unittest.TestCase):
    def test_CField(self):
        # Basic use
        class POINT(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.c_int)]
        pt = POINT(1, 2)
        self.assertEqual(pt.x, 1)
        self.assertEqual(pt.y, 2)

        # Invalid use
        self.assertRaises(TypeError, ctypes.CField, None)
        self.assertRaises(TypeError, ctypes.CField, [])
        self.assertRaises(TypeError, ctypes.CField, ())
        self.assertRaises(TypeError, ctypes.CField, {})
        self.assertRaises(TypeError, ctypes.CField, 1)
        self.assertRaises(TypeError, ctypes.CField, 1.0)
        self.assertRaises(TypeError, ctypes.CField, "")
        self.assertRaises(Type
