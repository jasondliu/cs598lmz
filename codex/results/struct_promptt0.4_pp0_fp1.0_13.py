import _struct
# Test _struct.Struct with a format that is not a string
try:
    _struct.Struct(42)
except TypeError:
    pass
else:
    print('TypeError expected')

# Test _struct.Struct with a format that is not a valid format string
try:
    _struct.Struct('z')
except ValueError:
    pass
else:
    print('ValueError expected')

# Test _struct.Struct with a format that is valid but not supported
try:
    _struct.Struct('c')
except ValueError:
    pass
else:
    print('ValueError expected')

# Test _struct.Struct with a format that is valid but not supported
try:
    _struct.Struct('?')
except ValueError:
    pass
else:
    print('ValueError expected')

# Test _struct.Struct with a format that is valid but not supported
try:
    _struct.Struct('b')
except ValueError:
    pass
else:
    print('ValueError expected')

# Test _struct.Struct with a format that is valid but not supported
try:
    _struct
