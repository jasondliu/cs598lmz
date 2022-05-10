import _struct
# Test _struct.Struct.format_size()

def test_format_size():
    # Test _struct.Struct.format_size() with various format strings
    for fmt in ['b', 'B', 'h', 'H', 'i', 'I', 'l', 'L', 'q', 'Q', 'f', 'd',
                's', 'p', 'P']:
        s = _struct.Struct(fmt)
        assert s.format_size() == s.size

def test_format_size_with_count():
    # Test _struct.Struct.format_size() with various format strings
    for fmt in ['b', 'B', 'h', 'H', 'i', 'I', 'l', 'L', 'q', 'Q', 'f', 'd',
                's', 'p', 'P']:
        s = _struct.Struct(fmt)
        assert s.format_size(10) == 10 * s.size

