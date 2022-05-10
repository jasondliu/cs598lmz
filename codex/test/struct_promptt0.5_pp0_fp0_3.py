import _struct
# Test _struct.Struct

def test_struct_bool():
    S = _struct.Struct("?")
    assert S.size == 1
    assert S.pack(True) == b"\x01"
    assert S.pack(False) == b"\x00"
    assert S.unpack(b"\x01") == (True,)
    assert S.unpack(b"\x00") == (False,)
    raises(struct.error, S.pack, "")
    raises(struct.error, S.pack, "x")
    raises(struct.error, S.pack, "abc")
    raises(struct.error, S.pack, "0")
    raises(struct.error, S.pack, "1")
    raises(struct.error, S.pack, "12")
    raises(struct.error, S.pack, "123")
    raises(struct.error, S.pack, "1234")
    raises(struct.error, S.pack, "12345")
    raises(struct.error, S.pack, "123456")
