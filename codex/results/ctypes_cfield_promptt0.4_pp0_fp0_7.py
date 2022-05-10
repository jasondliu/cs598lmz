import ctypes
# Test ctypes.CField
class CFieldTestCase(unittest.TestCase):
    def test_cfield(self):
        class foo(ctypes.Structure):
            _fields_ = [("bar", ctypes.c_int)]
        self.assertEqual(foo.bar.__class__, ctypes.CField)
        self.assertEqual(foo.bar.type, ctypes.c_int)

        self.assertRaises(AttributeError, getattr, foo, "bar")
        self.assertRaises(AttributeError, getattr, foo, "bar")

        foo._fields_ = [("bar", ctypes.c_char)]
        self.assertEqual(foo.bar.__class__, ctypes.CField)
        self.assertEqual(foo.bar.type, ctypes.c_char)
        self.assertRaises(AttributeError, getattr, foo, "bar")
        self.assertRaises(AttributeError, getattr, foo, "bar")

# Test ctypes.CField.from_address
class CFieldFromAddressTestCase(unitt
