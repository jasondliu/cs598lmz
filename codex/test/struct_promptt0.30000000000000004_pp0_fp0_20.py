import _struct
# Test _struct.Struct

# Test _struct.Struct.format
# Test _struct.Struct.size
# Test _struct.Struct.pack
# Test _struct.Struct.unpack
# Test _struct.Struct.pack_into
# Test _struct.Struct.unpack_from

def test_struct_format():
    assert _struct.Struct('@').format == '@'
    assert _struct.Struct('<').format == '<'
    assert _struct.Struct('>').format == '>'
    assert _struct.Struct('=').format == '='
    assert _struct.Struct('!').format == '!'
    assert _struct.Struct('x').format == 'x'
    assert _struct.Struct('c').format == 'c'
    assert _struct.Struct('b').format == 'b'
    assert _struct.Struct('B').format == 'B'
    assert _struct.Struct('h').format == 'h'
    assert _struct.Struct('H').format == 'H'
    assert _struct.Struct('i').format == 'i'
