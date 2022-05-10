import _struct
# Test _struct.Struct

# Test pack
for fmt in ['b', 'B', 'h', 'H', 'i', 'I', 'l', 'L', 'q', 'Q', 'f', 'd']:
    s = _struct.Struct(fmt)
    print(s.size, s.pack(0))

for fmt in ['c', 's', 'p', 'P']:
    s = _struct.Struct(fmt)
    print(s.size, s.pack(b''))

# Test unpack
for fmt, value in [('b', b'\x00'), ('B', b'\x00'), ('h', b'\x00\x00'),
                   ('H', b'\x00\x00'), ('i', b'\x00\x00\x00\x00'),
                   ('I', b'\x00\x00\x00\x00'), ('l', b'\x00\x00\x00\x00'),
                   ('L', b'\x00\x00\x00\x00'), ('q', b'\
