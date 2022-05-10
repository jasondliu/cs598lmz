import _struct
# Test _struct.Struct
def test__struct_Struct():
    S = _struct.Struct("ihhid")
    L = [1, 2, 3, -4, 5.0]
    s = b"A\x00\x00\x00\x02B\x00\x00\x00\x03C\x00\x00\x00\xfc\xff\xff\xffE\x00\x00\x00\x00\00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
    assert S.size == 20
    assert S.pack(*L) == s
    assert S.unpack(s) == L
    assert S.format == "=ihhid"
    assert S.unpack_from(s) == L
    raises(struct.error, S.unpack, b"")
    raises(struct.error, S.unpack, b"X"*19)
    raises(struct.error, S.unpack, b"X"*21)

    S = _
