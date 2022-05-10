import _struct
# Test _struct.Struct

# Test the basic types

for format in ['x', 'c', 'b', 'B', '?', 'h', 'H', 'i', 'I', 'l', 'L', 'q', 'Q',
               'f', 'd', 's', 'p', 'P']:
    s = _struct.Struct(format)
