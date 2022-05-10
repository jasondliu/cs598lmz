import ctypes
# Test ctypes.CField


class _TestCField(unittest.TestCase):
    def test_CField_invalid_type(self):
        with self.assertRaisesRegex(TypeError, "must be a ctypes type"):
            ctypes.CField(ctypes.c_int, "foo", "bar")

    def test_CField_invalid_offset(self):
        with self.assertRaisesRegex(TypeError, "must be an integer"):
            ctypes.CField(ctypes.c_int, "foo", "bar")

    def test_CField_invalid_bits(self):
        with self.assertRaisesRegex(TypeError, "must be an integer"):
            ctypes.CField(ctypes.c_int, "foo", "bar")

    def test_CField_invalid_bits_non_bitfield(self):
        with self.assertRaisesRegex(ValueError, "must be 0"):
            ctypes.CField(ctypes.c_int, "foo", "bar", size=4, bits=4
