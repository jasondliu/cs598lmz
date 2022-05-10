import _struct
# Test _struct.Struct.

import sys

# Test _struct.Struct.

def test_struct_unpack():
    s = _struct.Struct('i')
    values = s.unpack_from(b'\x01\x00\x00\x00')
    assert values == (1,)
    values = s.unpack_from(b'\x01\x00\x00\x00', 1)
    assert values == ()
    values = s.unpack_from(b'\x01\x00\x00\x00', 4)
    assert values == ()

    s = _struct.Struct('ii')
    values = s.unpack_from(b'\x01\x00\x00\x00\x02\x00\x00\x00')
    assert values == (1, 2)
    values = s.unpack_from(b'\x01\x00\x00\x00\x02\x00\x00\x00', 1)
    assert values == ()
    values = s.unpack_from(b'\
