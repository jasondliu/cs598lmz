import ctypes
# Test ctypes.CField here as well.
Field = ctypes.CField


class TestCase(unittest.TestCase):
    def test_repr(self):
        field = Field(ctypes.c_uint16, "age")
        self.assertEqual(repr(field), "CField(ctypes.c_uint16, 'age')")

    def test_offset(self):
        class S(ctypes.Structure):
            _fields_ = [
                ('foo', ctypes.c_uint8),
                ('bar', ctypes.c_uint16, 8),
            ]

        s = S()
        self.assertEqual(s.bar, 0)
        s.bar = 0x1234
        self.assertEqual(s.bar, 0x1234)

    def test_array(self):
        a = (ctypes.c_uint16 * 3)()
        a[:] = [1, 2, 3]
        self.assertEqual(list(a), [1, 2, 3])

    def test_default_value(self):
       
