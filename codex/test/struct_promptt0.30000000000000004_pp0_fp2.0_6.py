import _struct
# Test _struct.Struct.format

# Create a struct with a format that has a valid alignment specifier.
# The alignment specifier is ignored, but should not cause an error.
s = _struct.Struct('@i')
s.pack(1)

# Create a struct with a format that has an invalid alignment specifier.
# An error should be raised.
try:
    s = _struct.Struct('=i')
except TypeError:
    pass
else:
    print('TypeError not raised')
