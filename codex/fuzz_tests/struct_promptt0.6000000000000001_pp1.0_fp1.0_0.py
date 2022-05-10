import _struct
# Test _struct.Struct functions

# Test that the format string is parsed correctly
for format, size, alignment in [('x', 1, 1),
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
                                ('s', 1, 1),
                                ('p', 1, 1),
                                ('P', 4, 4),
                                ('?', 1, 1),
                                ('@', 0, 1),
                                ('=', 0, 1),
                                ('<', 0, 1),
                                ('>', 0, 1),
                                ('!', 0, 1),
                                ('xcb', 3
