import ctypes
# Test ctypes.CField

class TestCField(unittest.TestCase):
    def test_simple(self):
        class foo(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int)]
        self.assertEqual(foo.a.offset, ctypes.sizeof(ctypes.c_int))

    def test_simple_1(self):
        class foo(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int)]
        self.assertEqual(foo.b.offset, ctypes.sizeof(ctypes.c_int) * 2)

    def test_simple_2(self):
        class foo(ctypes.Structure):
            _fields_ = [("a", ctypes.c_int),
                        ("b", ctypes.c_int),
                        ("c", ctypes.c_int)]
        self.assertEqual(foo.c.offset, ctypes.sizeof(ctypes.c_int) * 3)

    def test
