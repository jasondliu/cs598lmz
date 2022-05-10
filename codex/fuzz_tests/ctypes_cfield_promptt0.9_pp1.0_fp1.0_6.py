import ctypes
# Test ctypes.CFields
class TestCF(unittest.TestCase):
    def test_value(self):
        a = ctypes.CFields('a', 'b')
        self.assertEqual(a.a, 'a')
        self.assertEqual(a.b, 'b')
        self.assertRaises(AttributeError, getattr, a, 'c')
        c = ctypes.CFields(x=17)
        self.assertEqual(c.x, 17)
        self.assertRaises(AttributeError, getattr, c, 'y')
        d = ctypes.CFields(17, 'xyzzy')
        self.assertEqual(d[0], 17)
        self.assertEqual(d[1], 'xyzzy')
        self.assertEqual(d.x, 17)
        self.assertEqual(d.y, 'xyzzy')
        self.assertRaises(TypeError, ctypes.CFields, 17, None)
        self.assertRaises(TypeError, ctypes.CFields, None, None)
