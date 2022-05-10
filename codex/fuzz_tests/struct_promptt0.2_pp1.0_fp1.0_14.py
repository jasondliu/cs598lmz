import _struct
# Test _struct.Struct.

# Test the basic functionality of _struct.Struct.

import _struct

def test_basic():
    s = _struct.Struct('i')
    assert s.size == 4
    assert s.pack(42) == b'*\x00\x00\x00'
    assert s.unpack(b'*\x00\x00\x00') == (42,)
    assert s.unpack_from(b'\x00\x00\x00*') == (42,)
    assert s.unpack_from(b'\x00\x00\x00*', 3) == (42,)
    assert s.unpack_from(b'\x00\x00\x00*', 4) == ()
    assert s.unpack_from(b'\x00\x00\x00*', 5) == ()
    assert s.unpack_from(b'\x00\x00\x00*', 6) == ()
    assert s.unpack_from(b'\x00\x00\x00*', 7) ==
