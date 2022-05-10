import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):

    def test_create_instance(self):

        class TestClass(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int)]

        class TestClass2(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int)]

        class TestClass3(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int)]

        c = ctypes.CField("f", TestClass, TestClass2, TestClass3, offset=1)
        self.assertEqual(c.name, "f")
        self.assertIs(c.ctype, TestClass)
        self.assertIs(c.ptrtype, TestClass2)
        self.assertIs(c.get_struct(), TestClass3)
        self.assertEqual(c.offset, 1)
        self.assertIs(c.ptr, 0)
        self.assertIs(c.dereference(), 0)
        self.assertFalse(c.is_
