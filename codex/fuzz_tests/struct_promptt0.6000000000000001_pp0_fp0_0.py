import _struct
# Test _struct.Struct.format

def test_format_sizeof_aligned():
    # Format strings should be padded to sizeof(int)
    for fmt in ['B', 'H', 'I', 'L', 'Q']:
        s = _struct.Struct('=%s' % fmt)
        assert s.size == _struct.calcsize('=' + fmt)
        assert s.size % _struct.calcsize('=I') == 0

def test_format_sizeof_unaligned():
    # Format strings should not be padded to sizeof(int)
    for fmt in ['b', 'h', 'i', 'l', 'q']:
        s = _struct.Struct('=%s' % fmt)
        assert s.size == _struct.calcsize('=' + fmt)
        assert s.size % _struct.calcsize('=I') == 0

def test_format_sizeof_char():
    # Format strings should not be padded to sizeof(int)
    for fmt in ['c', 's']:
        s = _struct.Struct('=%s' % fmt)
