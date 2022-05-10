import _struct
# Test _struct.Struct

tests = [
    ('b', 'a', 1, b'a'),
    ('b', 'a', 0, b'\0a'),
    ('b', 'a', -1, b'\xffa'),

    ('B', 'a', 1, b'a'),
    ('B', 'a', 0, b'\0a'),
    ('B', 'a', 255, b'\xffa'),

    ('h', 'a', 1, b'a'),
    ('h', 'a', 0, b'\0\0a'),
    ('h', 'a', -1, b'\xff\xffa'),

    ('H', 'a', 1, b'a'),
    ('H', 'a', 0, b'\0\0a'),
    ('H', 'a', 65535, b'\xff\xffa'),

    ('i', 'a', 1, b'a'),
    ('i', 'a', 0, b'\0\0\0\0a'),
    ('i', 'a', -1, b'\xff\xff\xff\
