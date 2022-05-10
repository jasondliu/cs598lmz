import _struct
# Test _struct.Struct.format_size

def test_format_size():
    s = _struct.Struct('hi')
    assert s.format_size() == 8
    assert s.size == 8
    s = _struct.Struct('hih')
    assert s.format_size() == 10
    assert s.size == 10
    s = _struct.Struct('b')
    assert s.format_size() == 1
    assert s.size == 1
    s = _struct.Struct('bx')
    assert s.format_size() == 2
    assert s.size == 2
    s = _struct.Struct('bxx')
    assert s.format_size() == 3
    assert s.size == 3
    s = _struct.Struct('bxxx')
    assert s.format_size() == 4
    assert s.size == 4
    s = _struct.Struct('bxxxx')
    assert s.format_size() == 5
    assert s.size == 5
    s = _struct.Struct('bxxxxx')
    assert s.format_size() == 6
    assert s
