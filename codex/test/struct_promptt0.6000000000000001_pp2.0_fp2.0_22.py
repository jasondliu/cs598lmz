import _struct
# Test _struct.Struct.format_map

# Test with a valid format string
s = _struct.Struct('f')
s.format_map('f')

# Test with an invalid format string
try:
    s.format_map('d')
except ValueError:
    pass
else:
    raise Exception

# Test with a non-string object
try:
    s.format_map(1)
except TypeError:
    pass
else:
    raise Exception

# Test with an empty string
try:
    s.format_map('')
except TypeError:
    pass
else:
    raise Exception

# Test with an empty format string
s = _struct.Struct('')
s.format_map('')
