import _struct
# Test _struct.Struct.

import struct

def test_struct():
    # test struct.Struct
    s = struct.Struct('hhl')
    s2 = struct.Struct('hhl')
    s3 = struct.Struct('hhl')
    assert s2 == s
    assert s2 == s3
    assert s == s3
    assert s == s2
    assert s != 'hhl'
    assert s != struct.Struct('hll')
    assert s != struct.Struct('hhll')
    assert s != struct.Struct('hh')
    assert s != struct.Struct('hhh')
    assert s != struct.Struct('hhhh')
    assert s.size == 8
    assert s.format == 'hhl'
    assert s.unpack(b'\x01\x02\x03\x04\x05\x06\x07\x08') == (0x0201, 0x0403, 0x06050407)
    assert s.pack(0x0201, 0x0403, 0x06050407) == b'\x01\x02\x03
