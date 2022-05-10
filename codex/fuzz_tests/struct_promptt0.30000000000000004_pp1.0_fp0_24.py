import _struct
# Test _struct.Struct.

# Test packing
#
# This is a list of (format, value, big_endian_result, little_endian_result)
# The big_endian_result is what you'd get on a big-endian machine.
# The little_endian_result is what you'd get on a little-endian machine.
#
# All test data is taken from the standard library test module test_struct.
#
# XXX: The test data is incomplete.

test_values = [
    ('x', b'G', b'G', b'G'),
    ('c', b'G', b'G', b'G'),
    ('b', 7, b'\x07', b'\x07'),
    ('B', 7, b'\x07', b'\x07'),
    ('h', 700, b'\x02\x8c', b'\x8c\x02'),
    ('H', 700, b'\x02\x8c', b'\x8c\x02'),
    ('i', 70000, b'\x00\
