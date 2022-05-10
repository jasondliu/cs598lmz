import _struct
# Test _struct.Struct

def test_struct_bool():
    for fmt in '?', 'B':
        s = _struct.Struct(fmt)
        assert s.size == 1
        assert s.pack(True) == b'\x01'
        assert s.pack(False) == b'\x00'
        assert s.unpack(b'\x00') == (False,)
        assert s.unpack(b'\x01') == (True,)
        assert s.unpack(b'\x02') == (True,)
        assert s.unpack(b'\xff') == (True,)
        assert s.unpack(b'\x00\x00') == (False,)
        assert s.unpack(b'\x00\x01') == (False,)
        assert s.unpack(b'\x01\x00') == (True,)
        assert s.unpack(b'\x01\x01') == (True,)
        assert s.unpack(b'\x02\x00') == (True,)
