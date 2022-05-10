import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_simple(self):
        class foo(ctypes.Structure):
            _fields_ = [("bar", ctypes.c_int)]
        self.assertEqual(foo.bar.offset, 0)
        self.assertEqual(foo.bar.size, ctypes.sizeof(ctypes.c_int))
        self.assertEqual(foo.bar.index, 0)
        self.assertEqual(foo.bar.pack, 1)
        self.assertEqual(foo.bar.type, ctypes.c_int)
        self.assertEqual(foo.bar.name, "bar")
        self.assertEqual(foo.bar.bitsize, 0)
        self.assertEqual(foo.bar.flags, 0)
        self.assertEqual(foo.bar.alignment, ctypes.alignment(ctypes.c_int))

    def test_simple_with_offset(self):
        class foo(ctypes.Structure):
            _fields_ = [("
