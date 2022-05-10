import _struct
# Test _struct.Struct with a format that is not a string
try:
    _struct.Struct(1)
except TypeError:
    pass
else:
    print('TypeError expected')

# Test _struct.Struct with a format that is not a valid format string
try:
    _struct.Struct('1')
except ValueError:
    pass
else:
    print('ValueError expected')

# Test _struct.Struct with a format that is not a valid format string
try:
    _struct.Struct('1x')
except ValueError:
    pass
else:
    print('ValueError expected')

# Test _struct.Struct with a format that is not a valid format string
try:
    _struct.Struct('1x1')
except ValueError:
    pass
else:
    print('ValueError expected')

# Test _struct.Struct with a format that is not a valid format string
try:
    _struct.Struct('1x1x')
except ValueError:
    pass
else:
    print('ValueError expected')

# Test _struct.Struct with a format that is not a
