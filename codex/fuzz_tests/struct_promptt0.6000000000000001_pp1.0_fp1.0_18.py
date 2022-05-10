import _struct
# Test _struct.Struct
def test_Struct_basic():
    Str = _struct.Struct('4s4s')
    s = Str.pack('abcd', 'efgh')
    assert s == 'abcd\x00efgh\x00'
    assert Str.unpack(s) == ('abcd', 'efgh')
    assert Str.unpack_from(s) == ('abcd', 'efgh')

def test_Struct_basic_format():
    Str = _struct.Struct('4s4s')
    assert Str.format == '4s4s'
    assert Str.size == 8
    assert Str.alignment == 1

def test_Struct_basic_format_native():
    Str = _struct.Struct('4s4s', _struct.NATIVE_ENDIAN)
    assert Str.format == '4s4s'
    assert Str.size == 8
    assert Str.alignment == 1

def test_Struct_basic_format_big():
    Str = _struct.Struct('4s4s', _struct.BIG_ENDIAN)
    assert Str.
