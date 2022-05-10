import _struct
# Test _struct.Struct.format

# Test that a format string is accepted and that the resulting object
# can be used to format data.

test_format = 'hhl5s'

s = _struct.Struct(test_format)

# Test that __doc__ is set
assert s.__doc__ == 'Compiled struct object'

assert s.format == test_format

# Test that the resulting object has the proper attributes
assert s.size == _struct.calcsize(test_format)
assert s.alignment == _struct.calcsize('ii')

# Test that the resulting object can be used to format data
assert s.pack(1, 2, 3, b'four') == b'\x01\x00\x02\x00\x00\x00\x00\x00\x03\x00\x00\x00four\x00\x00\x00\x00'
