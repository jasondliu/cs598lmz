import _struct
# Test _struct.Struct.format_size()

def test_format_size():
    s = _struct.Struct('i')
    assert s.size == s.format_size()
    assert s.format_size() == 4
    s = _struct.Struct('ii')
    assert s.size == s.format_size()
    assert s.format_size() == 8
    s = _struct.Struct('iih')
    assert s.size == s.format_size()
    assert s.format_size() == 10
    s = _struct.Struct('b')
    assert s.size == s.format_size()
    assert s.format_size() == 1
    s = _struct.Struct('b' * 10)
    assert s.size == s.format_size()
    assert s.format_size() == 10
    s = _struct.Struct('b' * 100)
    assert s.size == s.format_size()
    assert s.format_size() == 100
    s = _struct.Struct('b' * 1000)
    assert s.size == s.format_
