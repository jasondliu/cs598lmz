import _struct
# Test _struct.Struct class

def test_struct_simple():
    s = _struct.Struct("l")
    assert s.size == 4
    assert s.format == "l"
    assert s.pack(1) == "\x01\x00\x00\x00"
    assert s.unpack("\x01\x00\x00\x00") == (1,)

def test_struct_with_name():
    s = _struct.Struct("l", "name")
    assert s.size == 4
    assert s.format == "l"
    assert s.pack(1) == "\x01\x00\x00\x00"
    assert s.unpack("\x01\x00\x00\x00") == (1,)
    assert s.name == "name"

def test_struct_with_name_and_endianness():
    s = _struct.Struct("<l", "name")
    assert s.size == 4
    assert s.format == "<l"
    assert s.pack(1) == "\x01\x00\x
