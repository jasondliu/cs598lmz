import _struct
# Test _struct.Struct

def test_struct():
    from _struct import Struct
    from binascii import hexlify

    s = Struct('i')
    assert s.size == 4
    assert s.format == 'i'
    assert s.pack(1) == b'\x01\x00\x00\x00'
    assert s.unpack(s.pack(1)) == (1,)
    assert s.pack_into(bytearray(12), 4, 1) == None
    assert hexlify(bytearray(12)) == b'0000000001000000'
    assert s.unpack_from(bytearray(b'\x01\x00\x00\x00'), 0) == (1,)
    assert s.unpack_from(bytearray(b'\x00\x00\x00\x01'), 0) == (1,)
    assert s.unpack_from(bytearray(b'\x00\x00\x00\x01'), 0, 1) == (1,)
    assert s.unpack_from
