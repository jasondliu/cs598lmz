import _struct
# Test _struct.Struct

def test_struct_unpack():
    s = _struct.Struct('i')
    assert s.size == 4
    assert s.pack(1) == b'\x01\x00\x00\x00'
    assert s.pack_into(bytearray(b'xxxx'), 1, 2) == None
    assert s.unpack(b'\x01\x00\x00\x00') == (1,)
    assert s.unpack_from(b'xx\x01\x00\x00\x00', 2) == (1,)

def test_struct_pack_into():
    s = _struct.Struct('i')
    b = bytearray(b'xxxx')
    assert s.pack_into(b, 1, 2) == None
    assert b == bytearray(b'x\x02\x00\x00\x00')
    assert s.pack_into(b, 1, 3, True) == None
    assert b == bytearray(b'x\x03\x00\x00
