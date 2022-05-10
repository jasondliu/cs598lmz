import _struct
# Test _struct.Struct.

for cls in [_struct.Struct, _struct.Struct_byteorder]:
    s = cls('i')
    assert s.size == _struct.calcsize('i')
    assert not s.unpack('\x00\x00\x00\x00')
    assert s.unpack(_struct.pack('i', 1)) == (1,)
    assert s.unpack(_struct.pack('i', -1)) == (-1,)
    assert s.unpack(_struct.pack('i', 0x7fffffff)) == (0x7fffffff,)
    assert s.unpack(_struct.pack('i', -0x80000000)) == (-0x80000000,)

    s = cls('i', 'big')
    assert s.size == _struct.calcsize('i')
    assert not s.unpack('\x00\x00\x00\x00')
    assert s.unpack(_struct.pack('>i', 1)) == (1,)
    assert s.unpack(_struct.pack('>i', -1)) == (-1
