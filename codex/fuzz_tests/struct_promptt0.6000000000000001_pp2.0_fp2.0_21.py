import _struct
# Test _struct.Struct

# Test basic packing and unpacking
for fmt, expected in [
        ('', b''),
        ('1s', b'x'),
        ('4s', b'xxxx'),
        ('c', b'x'),
        ('cx', b'x'),
        ('h', b'\x12\x34'),
        ('h2s', b'\x12\x34xx'),
        ('l', b'\x12\x34\x56\x78'),
        ('l2s', b'\x12\x34\x56\x78xx'),
        ('q', b'\x12\x34\x56\x78\x9a\xbc\xde\xf0'),
        ('q2s', b'\x12\x34\x56\x78\x9a\xbc\xde\xf0xx'),
        ('f', b'\x00\x00\x80@'),
        ('d', b'@\x00\x00\x00\x00\x00\x00\x00'),
        ('
