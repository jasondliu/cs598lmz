import _struct
# Test _struct.Struct

# Test _struct.Struct

import _struct

def test_struct():
    s = _struct.Struct("hi")
    assert s.size == 2
    assert s.pack(1, 2) == b"\x01\x00\x02\x00"
    assert s.unpack(b"\x01\x00\x02\x00") == (1, 2)
    assert s.unpack_from(b"\x01\x00\x02\x00") == (1, 2)
    assert s.unpack_from(b"\x01\x00\x02\x00", 1) == (2,)
    assert s.unpack_from(b"\x01\x00\x02\x00", 1, 1) == ()
    assert s.unpack_from(b"\x01\x00\x02\x00", 1, 2) == (2,)
    assert s.unpack_from(b"\x01\x00\x02\x00", 1, 3) == (2,)
   
