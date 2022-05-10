import _struct
# Test _struct.Struct.
# Expect byte sequence of the right length
# and one exception
ok = 0
err = 0
for fmt, length in [
    ('i', 4),
    ('ii', 8),
    ('l', 4),
    ('ll', 8),
    ('h', 2),
    ('hh', 4),
    ('b', 1),
    ('bb', 2),
    ('4h', 8),
    ('3i', 12),
    ('f', 4),
    ('d', 8),
    ('xi', 4),
]:
    s = _struct.Struct(fmt)
