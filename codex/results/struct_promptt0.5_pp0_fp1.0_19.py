import _struct
# Test _struct.Struct.

# format:
# (format, (args), (expected result))
test_values = [
    ('i', (1,), '\x01\x00\x00\x00'),
    ('i', (-1,), '\xff\xff\xff\xff'),
    ('i', (2**31,), '\x80\x00\x00\x00'),
    ('i', (-2**31,), '\x80\x00\x00\x01'),
    ('i', (2**32-1,), '\xff\xff\xff\xff'),
    ('i', (-2**32,), '\x00\x00\x00\x00'),
    ('i', (2**32,), OverflowError),
    ('i', (-2**32-1,), OverflowError),
    ('i', (2L**31,), '\x80\x00\x00\x00'),
    ('i', (-2L**31,), '\x80\x00\x00\x01'),
    ('i', (2L
