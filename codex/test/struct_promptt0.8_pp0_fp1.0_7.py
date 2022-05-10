import _struct
# Test _struct.Struct
class TestStruct:
    def test_init(self):
        Str = _struct.Struct("i")
        assert Str.size == _struct.calcsize("i")
        assert Str.format == "i"
        assert Str.format_char == "i"
        assert Str.unpack == _struct.unpack
        assert Str.pack == _struct.pack
        assert Str._cache == {}
        Str = _struct.Struct("10s")
        assert Str.size == _struct.calcsize("10s")
        assert Str.format == "10s"
        assert Str.format_char == "10s"
        assert Str.unpack == _struct.unpack
        assert Str.pack == _struct.pack
        assert Str._cache == {}
        assert repr(Str) == "<Struct format:10s>"
        Str = _struct.Struct("<4p")
        assert Str.format_char == "4p"
        assert type(Str.format) is bytes
        assert Str.size == _struct.calcsize("<4p")
        assert Str.un
