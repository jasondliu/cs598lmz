import ctypes
# Test ctypes.CField

class TestCField(unittest.TestCase):
    def test_simple_field(self):
        class foo(ctypes.Structure):
            _fields_ = [("bar", ctypes.c_int)]

        f = foo()
        self.assertEqual(f.bar, 0)

    def test_simple_field_with_value(self):
        class foo(ctypes.Structure):
            _fields_ = [("bar", ctypes.c_int, 42)]

        f = foo()
        self.assertEqual(f.bar, 42)

    def test_simple_field_with_value_and_offset(self):
        class foo(ctypes.Structure):
            _fields_ = [("bar", ctypes.c_int, 42, 4)]

        f = foo()
        self.assertEqual(f.bar, 42)

    def test_subclass(self):
        class foo(ctypes.Structure):
            _fields_ = [("bar", ctypes.c_int)]

        class bar(foo):
           
