import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_CField(self):
        class c(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int)]
        self.assertEqual(c.x.offset, 0)
        self.assertEqual(c.x.size, ctypes.sizeof(ctypes.c_int))

    def test_CField_name(self):
        class c(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int)]
        self.assertEqual(c.x.__name__, "x")
        # The __name__ attribute is used to build the repr string
        self.assertEqual(repr(c.x), "<Field type=c_int, ofs=0, size=4>")

    def test_CField_invalid_name(self):
        class c(ctypes.Structure):
            pass
        with self.assertRaises(TypeError):
            c.x = ctypes.c_int()

