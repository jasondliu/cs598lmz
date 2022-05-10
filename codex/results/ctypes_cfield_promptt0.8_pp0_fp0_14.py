import ctypes
# Test ctypes.CField


class TestCField(unittest.TestCase):

    def test_none(self):
        with self.assertRaises(TypeError):
            ctypes.CField(None)

    def test_len(self):
        self.assertEqual(len(ctypes.CField('a[3]')), 4)
        self.assertEqual(len(ctypes.CField('a[4]')), 4)
        self.assertEqual(len(ctypes.CField('a[5]')), 8)
        self.assertEqual(len(ctypes.CField('a[6]')), 8)

    def test_as_parameter(self):
        self.assertRaises(TypeError, ctypes.CField('a')._as_parameter_)

    def test_str(self):
        self.assertRaises(NotImplementedError, str, ctypes.CField('a'))

    def test_repr(self):
        with self.assertRaises(NotImplementedError):
            repr(ctypes.CField
