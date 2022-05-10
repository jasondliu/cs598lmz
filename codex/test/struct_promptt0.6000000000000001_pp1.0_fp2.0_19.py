import _struct
# Test _struct.Struct().format_size()
for fmt, size in [
    ('b', 1),
    ('h', 2),
    ('i', 4),
    ('l', 4),
    ('q', 8),
    ('B', 1),
    ('H', 2),
    ('I', 4),
    ('L', 4),
    ('Q', 8),
    ('f', 4),
    ('d', 8),
    ('s', 8),
    ('p', 1),
    ('P', 4),
    ('c', 1),
]:
    assert _struct.Struct(fmt).format_size() == size
# Test _struct.Struct().size
