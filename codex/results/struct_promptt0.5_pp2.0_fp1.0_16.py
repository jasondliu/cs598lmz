import _struct
# Test _struct.Struct

for fmt in ['x', 'c', 'b', 'B', 'h', 'H', 'i', 'I', 'l', 'L', 'q', 'Q', 'f', 'd', 's', 'p']:
    print fmt, _struct.calcsize(fmt)
