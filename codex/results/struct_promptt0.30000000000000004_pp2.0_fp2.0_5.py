import _struct
# Test _struct.Struct

def unpack(fmt, data):
    return _struct.unpack(fmt, data)

def pack(fmt, *data):
    return _struct.pack(fmt, *data)

def calcsize(fmt):
    return _struct.calcsize(fmt)

def test_unpack():
    assert unpack('hi', b'\x01\x00\x02\x00') == (1, 2)
    assert unpack('h', b'\x01\x00') == (1,)
    assert unpack('h', b'\x01\x00\x02\x00') == (1,)
    assert unpack('h', b'\x01\x00\x02\x00', 1) == (2,)
    assert unpack('h', b'\x01\x00\x02\x00', 1, 1) == ()
    assert unpack('h', b'\x01\x00\x02\x00', 1, 2) == (2,)
    assert unpack('h', b
