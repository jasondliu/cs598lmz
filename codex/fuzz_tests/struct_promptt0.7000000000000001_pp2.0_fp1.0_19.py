import _struct
# Test _struct.Struct

class StructTest(unittest.TestCase):
    # We don't test unpack_from or calcsize or any of the optional args
    # to __init__; it's not clear that there's any good way to do that.
    # (And we're not going to replicate all the struct module tests here.)

    def test_simple_pack(self):
        s = _struct.Struct('i')
        self.assertEqual(s.pack(12345), b'@I\x00\x00')

    def test_simple_unpack(self):
        s = _struct.Struct('i')
        self.assertEqual(s.unpack(b'@I\x00\x00'), (12345,))

    def test_simple_pack_into(self):
        s = _struct.Struct('i')
        buf = bytearray(8)
        s.pack_into(buf, 0, 12345)
        self.assertEqual(buf, b'@I\x00\x00\x00\x00\x00\x00
