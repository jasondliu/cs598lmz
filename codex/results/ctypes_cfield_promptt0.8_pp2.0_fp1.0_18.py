import ctypes
# Test ctypes.CField(..., ctypes.Structure)
#

class Test_CField(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_field_named(self):
        class Bar(ctypes.Structure):
            _fields_ = [("foo", ctypes.c_int)]

        class Bar2(ctypes.Structure):
            _fields_ = [("foo", ctypes.c_int), ("bar", ctypes.Structure)]

        self.assertRaises(AttributeError, getattr, Bar2(), "foo")
        #self.assertRaises(ValueError, ctypes.Structure, "foo")
        b = Bar()
        self.assertEqual(b.foo, 0)

    def test_field_unnamed(self):
        class Bar(ctypes.Structure):
            _fields_ = [("", ctypes.c_int)]

        self.assertRaises(AttributeError, getattr, Bar(), "")
        self.assertRaises(ValueError, ctypes
