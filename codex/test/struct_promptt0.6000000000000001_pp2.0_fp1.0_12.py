import _struct
# Test _struct.Struct.format_length()

def test_format_length():
    s = _struct.Struct('c')
    assert s.format_length() == 1
    s = _struct.Struct('cc')
    assert s.format_length() == 2
    s = _struct.Struct('ccc')
    assert s.format_length() == 3
    s = _struct.Struct('csc')
    assert s.format_length() == 3
    s = _struct.Struct('cscs')
    assert s.format_length() == 4
    s = _struct.Struct('cscsI')
    assert s.format_length() == 8
    s = _struct.Struct('cscsIQ')
    assert s.format_length() == 16
    s = _struct.Struct('cscsIQP')
    assert s.format_length() == 24
    s = _struct.Struct('cscsIQPx')
    assert s.format_length() == 24
    s = _struct.Struct('cscsIQPxQ')
    assert s.format_length
