import _struct
# Test _struct.Struct.format_size()

import _struct

# Check that the format_size() method returns the correct value for all
# standard struct formats.
for fmt in 'bBhHiIlLfd':
    s = _struct.Struct(fmt)
    assert s.format_size() == _struct.calcsize(fmt)

# Check that format_size() returns the correct value for a non-standard
# format.
s = _struct.Struct('@')
assert s.format_size() == 0

# Check that format_size() returns the correct value for a multi-byte format.
s = _struct.Struct('=I')
assert s.format_size() == 4

# Check that format_size() returns the correct value for a format with
# multiple format characters.
s = _struct.Struct('=Ih')
assert s.format_size() == 6

# Check that format_size() returns the correct value for a format with
# multiple format characters and a non-standard format character.
s = _struct.Struct('@Ih')
assert s.format_size()
