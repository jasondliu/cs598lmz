import _struct
# Test _struct.Struct.format_size() with the various alignment
# requirements:
for fmt in ['', '@', '=', '<', '>', '!', '<@', '>@', '<@>', '>@<']:
    s = _struct.Struct('0s%s' % fmt)
    assert s.format_size() == 1, fmt
    s = _struct.Struct('1s%s' % fmt)
    assert s.format_size() == 1, fmt
    s = _struct.Struct('2s%s' % fmt)
    assert s.format_size() == 2, fmt
    s = _struct.Struct('3s%s' % fmt)
    assert s.format_size() == 4, fmt
    s = _struct.Struct('4s%s' % fmt)
    assert s.format_size() == 4, fmt
    s = _struct.Struct('5s%s' % fmt)
    assert s.format_size() == 8, fmt
    s = _struct.Struct('6s%s' % fmt)
    assert s.format
