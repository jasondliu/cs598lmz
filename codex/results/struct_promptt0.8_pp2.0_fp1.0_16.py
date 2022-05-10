import _struct
# Test _struct.Struct

def test_struct(cls, pack_args, pack_fmt, unpack_args, unpack_fmt, expected_result):

    s = cls(pack_fmt)
    packed = s.pack(*pack_args)
    assert len(packed) == s.size
    unpacked = s.unpack(packed)
    assert unpacked == expected_result
    assert s.pack_into(*(pack_args + (bytearray(s.size), 0))) == None
    assert s.unpack_from(packed, 0) == expected_result

    if unpack_fmt:
        s = cls(unpack_fmt)
        unpacked_args = s.unpack(*unpack_args)
        assert len(packed) == s.size
        assert unpacked == expected_result
        assert s.pack_into(*(unpacked_args + (bytearray(s.size), 0))) == None
        assert s.unpack_from(packed, 0) == expected_result

    # Issue #17809: struct.calcsize()
