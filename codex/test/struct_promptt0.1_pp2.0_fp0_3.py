import _struct
# Test _struct.Struct

# Test _struct.Struct

import _struct

def test_struct_basic():
    s = _struct.Struct('i')
    assert s.size == 4
    assert s.pack(42) == b'*\x00\x00\x00'
    assert s.unpack(b'*\x00\x00\x00') == (42,)
    assert s.unpack_from(b'\x00\x00\x00*') == (42,)
    assert s.unpack_from(b'\x00\x00\x00*', 3) == (42,)
    assert s.unpack_from(memoryview(b'\x00\x00\x00*'), 3) == (42,)
    assert s.unpack_from(bytearray(b'\x00\x00\x00*'), 3) == (42,)
    assert s.unpack_from(b'\x00\x00\x00*', 3, 1) == ()
