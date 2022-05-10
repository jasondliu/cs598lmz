import _struct
# Test _struct.Struct

test_support.import_module('_struct')

# note, we're testing both endiannesses for each type
tests = [
    ('x', b'x'),
    ('b', b'\x01'),
    ('B', b'\x01'),
    ('h', b'\x01\x00'),
    ('H', b'\x01\x00'),
    ('i', b'\x01\x00\x00\x00', 1),
    ('I', b'\x01\x00\x00\x00'),
    ('l', b'\x01\x00\x00\x00', 1),
    ('L', b'\x01\x00\x00\x00'),
    ('q', b'\x01\x00\x00\x00\x00\x00\x00\x00', 1),
    ('Q', b'\x01\x00\x00\x00\x00\x00\x00\x00'),
    ('f', b'\x00\x00\x
