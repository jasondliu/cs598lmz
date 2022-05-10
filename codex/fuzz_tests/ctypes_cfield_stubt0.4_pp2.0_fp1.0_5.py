import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class Test(unittest.TestCase):
    def test_field_type(self):
        self.assertEqual(ctypes.c_int, S.x.type)

    def test_field_name(self):
        self.assertEqual('x', S.x.name)

    def test_field_offset(self):
        self.assertEqual(0, S.x.offset)

    def test_field_index(self):
        self.assertEqual(0, S.x.index)

    def test_field_size(self):
        self.assertEqual(ctypes.sizeof(ctypes.c_int), S.x.size)

    def test_field_bits(self):
        self.assertEqual(ctypes.sizeof(ctypes.c_int) * 8, S.x.bits)

    def test_field_pack(self):
        self.assertEqual(1, S.x.pack)

if __name__ == "__main__":
    unittest.main()
