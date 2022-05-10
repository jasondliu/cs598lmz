import _struct
# Test _struct.Struct.

import _struct

def test():
    s = _struct.Struct('i')
    assert s.size == 4
    assert s.format == 'i'
    assert s.pack(1) == b'\x01\x00\x00\x00'
    assert s.pack(1, 2) == b'\x01\x00\x00\x00'
    assert s.unpack(b'\x01\x00\x00\x00') == (1,)
    assert s.unpack_from(b'\x01\x00\x00\x00') == (1,)
    assert s.unpack_from(b'\x01\x00\x00\x00', 0) == (1,)
    assert s.unpack_from(b'\x01\x00\x00\x00', 1) == (_struct.error,)
    assert s.unpack_from(b'\x01\x00\x00\x00', 0, True) == (1,)
    assert s.unpack_from(b
