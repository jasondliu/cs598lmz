import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int


class Test(unittest.TestCase):

    def test_from_buffer(self):
        buf = bytearray(b'\x01\x00\x00\x00')
        s = S.from_buffer(buf)
        self.assertEqual(s.x, 1)

        # Test that the buffer is still writable
        buf[0] = 0x34
        self.assertEqual(s.x, 52)

        # Test that the buffer is still writable after slicing
        buf = buf[2:]
        buf[0] = 0x56
        self.assertEqual(s.x, 86)

    def test_from_buffer_copy(self):
        buf = bytearray(b'\x01\x00\x00\x00')
        s = S.from_buffer_copy(buf)
        self.assertEqual(s.x, 1)

        # Test that the buffer is not writable
        self.assertRaises(TypeError, buf.__setitem__, 0,
