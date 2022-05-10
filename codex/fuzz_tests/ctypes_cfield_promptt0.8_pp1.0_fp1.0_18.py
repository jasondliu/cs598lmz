import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_c_field(self):
        c = ctypes.CField(ctypes.CField("a", ctypes.c_long), "b", ctypes.c_long)
        self.assertEqual(c.name, "a.b")
        self.assertEqual(c.ctype, ctypes.c_long)
        self.assertEqual(repr(c), "CField('%s', %r)" % ("a.b", ctypes.c_long))
        self.assertEqual(str(c), "CField('%s', %r)" % ("a.b", ctypes.c_long))
        self.assertRaises(TypeError, ctypes.CField, 1, 2, 3, 4)
        self.assertRaises(TypeError, ctypes.CField, "a", "b", "c")
        self.assertRaises(TypeError, ctypes.CField, "a", None, None)
    def test_c_field_bits(self):

