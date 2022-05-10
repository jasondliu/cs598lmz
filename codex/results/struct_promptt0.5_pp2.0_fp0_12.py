import _struct
# Test _struct.Struct.

import _struct

from test import support

def test_struct():
    # Simple tests for _struct.Struct objects.

    s = _struct.Struct("i")
    assert s.size == 4
    assert s.format == "i"
    assert s.pack(12345) == b"\x39\x30\x00\x00"
    assert s.unpack(b"\x39\x30\x00\x00") == (12345,)
    assert s.unpack_from(b"\x00\x00\x00\x00\x39\x30\x00\x00", 4) == (12345,)
    assert s.unpack_from(bytearray(b"\x00\x00\x00\x00\x39\x30\x00\x00"), 4) == (12345,)
    assert s.unpack_from(memoryview(b"\x00\x00\x00\x00\x39\x30\x00\x00"), 4) == (12345,)
   
