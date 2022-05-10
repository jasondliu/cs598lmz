import _struct
# Test _struct.Struct

class TestStruct:
    def setup_class(cls):
        cls.s = _struct.Struct('hhl')
        cls.s2 = _struct.Struct('hhl')
        cls.s3 = _struct.Struct('hhl')
        cls.s4 = _struct.Struct('hhl')

    def test_size(self):
        assert self.s.size == 8

    def test_pack(self):
        assert self.s.pack(1, 2, 3) == b'\x01\x00\x02\x00\x00\x00\x00\x03'

    def test_unpack(self):
        assert self.s.unpack(b'\x01\x00\x02\x00\x00\x00\x00\x03') == (1, 2, 3)

    def test_pack_into(self):
        buf = bytearray(8)
        self.s.pack_into(buf, 0, 1, 2, 3)
        assert buf == b'\x
