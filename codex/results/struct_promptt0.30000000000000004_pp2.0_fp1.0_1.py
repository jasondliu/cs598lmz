import _struct
# Test _struct.Struct

def test_struct_1():
    s = _struct.Struct("i")
    assert s.size == 4
    assert s.pack(12345) == b"\x39\x30\x00\x00"
    assert s.unpack(b"\x39\x30\x00\x00") == (12345,)

def test_struct_2():
    s = _struct.Struct("ii")
    assert s.size == 8
    assert s.pack(12345, 54321) == b"\x39\x30\x00\x00\x15\xAF\x00\x00"
    assert s.unpack(b"\x39\x30\x00\x00\x15\xAF\x00\x00") == (12345, 54321)

def test_struct_3():
    s = _struct.Struct("iii")
    assert s.size == 12
    assert s.pack(12345, 54321, 0) == b"\x39\x30\x00\x00\
