import _struct
# Test _struct.Struct.format_size.
def test_format_size():
    assert _struct.Struct('i').format_size('@') == 4
    assert _struct.Struct('i').format_size('=') == 4
    assert _struct.Struct('i').format_size('<') == 4
    assert _struct.Struct('i').format_size('>') == 4
    assert _struct.Struct('i').format_size('!') == 4
    assert _struct.Struct('i').format_size('@i') == 4
    assert _struct.Struct('i').format_size('=i') == 4
    assert _struct.Struct('i').format_size('<i') == 4
    assert _struct.Struct('i').format_size('>i') == 4
    assert _struct.Struct('i').format_size('!i') == 4
    assert _struct.Struct('i').format_size('@p') == 4
    assert _struct.Struct('i').format_size('=p') == 4
    assert _struct.Struct('i').format_size('<p') == 4

