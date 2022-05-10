import _struct
# Test _struct.Struct
with _struct.Struct('B') as s:
    assert s.size == 1
    assert s.pack(0) == b'\x00'
    assert s.unpack(b'\x00') == (0,)

with _struct.Struct('i') as s:
    assert s.size == 4
    assert s.pack(0) == b'\x00\x00\x00\x00'
    assert s.unpack(b'\x00\x00\x00\x00') == (0,)

with _struct.Struct('I') as s:
    assert s.size == 4
    assert s.pack(0) == b'\x00\x00\x00\x00'
    assert s.unpack(b'\x00\x00\x00\x00') == (0,)

print('pass')
