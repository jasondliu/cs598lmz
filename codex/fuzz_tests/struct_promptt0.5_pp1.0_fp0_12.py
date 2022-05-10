import _struct
# Test _struct.Struct.format_size()

# Test the basics
for fmt in ['x', 'c', 'b', 'B', 'h', 'H', 'i', 'I', 'l', 'L', 'q', 'Q', 'f', 'd']:
    s = _struct.Struct(fmt)
    assert s.format_size() == s.size

# Alignment
for fmt in ['b', 'B', 'h', 'H', 'i', 'I', 'l', 'L', 'q', 'Q', 'f', 'd']:
    s = _struct.Struct(fmt + 'x')
    assert s.format_size() == s.size

# Test packing of non-native byte order
for fmt in ['x', 'c', 'b', 'B', 'h', 'H', 'i', 'I', 'l', 'L', 'q', 'Q', 'f', 'd']:
    s = _struct.Struct('>' + fmt)
    assert s.format_size() == s.size

# Test packing of non-native byte order with alignment

