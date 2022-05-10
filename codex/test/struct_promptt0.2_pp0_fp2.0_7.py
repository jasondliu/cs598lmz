import _struct
# Test _struct.Struct.format_size()

def test_format_size():
    s = _struct.Struct('hhl')
    assert s.format_size('@') == 8
    assert s.format_size('=') == 8
    assert s.format_size('<') == 8
    assert s.format_size('>') == 8
    assert s.format_size('!') == 8
    assert s.format_size('@hhl') == 8
    assert s.format_size('=hhl') == 8
    assert s.format_size('<hhl') == 8
    assert s.format_size('>hhl') == 8
    assert s.format_size('!hhl') == 8
    assert s.format_size('@2h2l') == 8
    assert s.format_size('=2h2l') == 8
    assert s.format_size('<2h2l') == 8
    assert s.format_size('>2h2l') == 8
    assert s.format_size('!2h2l') == 8
