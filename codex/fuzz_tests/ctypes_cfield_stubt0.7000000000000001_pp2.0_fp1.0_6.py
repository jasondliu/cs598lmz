import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class Test(unittest.TestCase):
    def test_cfield_instance(self):
        self.assertIsInstance(S.x, ctypes.CField)

    @unittest.skip("XXX")
    def test_cfield_repr(self):
        self.assertEqual(repr(S.x), "<Field type=c_long, ofs=0x0, size=0x4>")

    def test_cfield_name(self):
        self.assertEqual(S.x.name, "x")

    def test_cfield_offset(self):
        self.assertEqual(S.x.offset, 0)

    def test_cfield_size(self):
        self.assertEqual(S.x.size, ctypes.sizeof(ctypes.c_int))

if __name__ == "__main__":
    unittest.main()
