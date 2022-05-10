import _struct
# Test _struct.Struct

# Test pack
for fmt in ['b', 'B', 'h', 'H', 'i', 'I', 'l', 'L', 'q', 'Q', 'f', 'd']:
    s = _struct.Struct(fmt)
    print(s.size, s.pack(0))

for fmt in ['c', 's', 'p', 'P']:
    s = _struct.Struct(fmt)
    print(s.size, s.pack(b''))

