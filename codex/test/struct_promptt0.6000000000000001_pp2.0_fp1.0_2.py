import _struct
# Test _struct.Struct

def test_struct_unpack():
    assert _struct.Struct('i').unpack(b'\x12\x34\x56\x78') == (305419896,)
    assert _struct.Struct('h').unpack(b'\x12\x34') == (4660,)
    assert _struct.Struct('H').unpack(b'\x12\x34') == (4660,)
    assert _struct.Struct('b').unpack(b'\x12') == (18,)
    assert _struct.Struct('B').unpack(b'\x12') == (18,)
    assert _struct.Struct('c').unpack(b'\x12') == (b'\x12',)
    assert _struct.Struct('s').unpack(b'\x12') == (b'\x12',)
    assert _struct.Struct('p').unpack(b'\x12') == (b'\x12',)
