import _struct

class TestStruct(unittest.TestCase):

    def test_unpack_from(self):
        # It is important that the buffer size be divisible by the
        # alignment.  The default buffer size is too small.
        buf = array.array('b', b'\x12\x34\x56\x78'*50)
        s = _struct.Struct('i')
        offset = 3
        for i in range(50):
            self.assertEqual(s.unpack_from(buf, offset), (0x12345678,))
            offset += 4

    def test_pack_into(self):
        # It is important that the buffer size be divisible by the
        # alignment.  The default buffer size is too small.
        buf = array.array('b', b'\x00\x00\x00\x00'*50)
        s = _struct.Struct('i')
        offset = 3
        for i in range(50):
            s.pack_into(buf, offset, 0x12345678)
            offset += 4
