import _struct
# Test _struct.Struct()

def pack(fmt, *args):
    return _struct.Struct(fmt).pack(*args)

def unpack(fmt, *args):
    return _struct.Struct(fmt).unpack(*args)

def calcsize(fmt):
    return _struct.Struct(fmt).size

def test_struct():
    assert pack("hhl", 1, 2, 3) == b"\x01\x00\x02\x00\x00\x00\x00\x03"
    assert unpack("hhl", b"\x01\x00\x02\x00\x00\x00\x00\x03") == (1, 2, 3)
    assert calcsize("hhl") == 8
    raises(struct.error, pack, "z", b"a") # 'z' is not supported
    raises(struct.error, pack, "t", 1) # 't' is not supported
    raises(struct.error, pack, "n", 1) # 'n' is not supported
