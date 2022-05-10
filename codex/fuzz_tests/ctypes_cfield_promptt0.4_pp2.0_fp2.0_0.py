import ctypes
# Test ctypes.CField
class _TestCField(ctypes.Structure):
    _fields_ = [('a', ctypes.c_char),
                ('b', ctypes.c_int)]

class TestCField(unittest.TestCase):
    def test_CField(self):
        # Test that the CField object is a class attribute of _TestCField
        self.assertTrue(hasattr(_TestCField, 'a'))
        self.assertTrue(hasattr(_TestCField, 'b'))
        self.assertTrue(isinstance(_TestCField.a, ctypes.CField))
        self.assertTrue(isinstance(_TestCField.b, ctypes.CField))
        self.assertEqual(_TestCField.a.offset, 0)
        self.assertEqual(_TestCField.b.offset, 1)

        # Test that the CField object is a class attribute of the _fields_ element
        self.assertTrue(hasattr(_TestCField._fields_[0], 'a'))
        self.assertTrue(hasattr(_TestCField._
