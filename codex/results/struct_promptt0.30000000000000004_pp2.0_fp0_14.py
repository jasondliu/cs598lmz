import _struct
# Test _struct.Struct
import _struct

def test_struct_unpack():
    s = _struct.Struct('i')
    assert s.size == 4
    assert s.pack(12345) == b'\x39\x30\x00\x00'
    assert s.unpack(b'\x39\x30\x00\x00') == (12345,)
    assert s.unpack_from(b'\x00\x00\x39\x30', 2) == (12345,)

def test_struct_pack():
    s = _struct.Struct('i')
    assert s.size == 4
    assert s.pack(12345) == b'\x39\x30\x00\x00'
    raises(struct.error, s.pack, 12345, 5)

def test_struct_iter_unpack():
    s = _struct.Struct('i')
    assert s.size == 4
    assert list(s.iter_unpack(b'\x39\x30\x00\x00\x00\x00\x39
