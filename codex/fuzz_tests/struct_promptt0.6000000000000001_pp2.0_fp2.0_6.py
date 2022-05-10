import _struct
# Test _struct.Struct
import _testcapi

def test_struct(type_char, expected_size):
    s = _struct.Struct(type_char)
    assert s.size == expected_size

def test_unpack():
    s = _struct.Struct("i")
    assert s.unpack("\x01\x00\x00\x00") == (1,)
    assert s.unpack("\x00\x00\x00\x00") == (0,)
    assert s.unpack("\xFF\xFF\xFF\xFF") == (-1,)
    assert s.unpack("\xFF\xFF\xFF\x7F") == (2147483647,)
    assert s.unpack("\x00\x00\x00\x80") == (-2147483648,)

def test_pack():
    s = _struct.Struct("i")
    assert s.pack(0) == "\x00\x00\x00\x00"
    assert s.pack(-1) == "\xFF\xFF\x
