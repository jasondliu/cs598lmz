import _struct
# Test _struct.Struct.

# The following is a list of all the standard format characters,
# as used by the struct module.  The first character is the format
# character, the second is the native size of the format (in bytes),
# and the third is the size of the format when packed.

format_sizes = [
    ('x', 0, 0),
    ('c', 1, 1),
    ('b', 1, 1),
    ('B', 1, 1),
    ('h', 2, 2),
    ('H', 2, 2),
    ('i', 4, 4),
    ('I', 4, 4),
    ('l', 4, 4),
    ('L', 4, 4),
    ('q', 8, 8),
    ('Q', 8, 8),
    ('f', 4, 4),
    ('d', 8, 8),
    ('s', 1, None),
    ('p', 1, None),
    ('P', 4, 4),
]

# The following is a list of all the standard format characters,
# as used by the struct module.  The first character is the
