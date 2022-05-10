import _struct
# Test _struct.Struct()

# Try a simple struct
s = _struct.Struct('i')

# Try a format that's too short
try:
    s = _struct.Struct('i')
except ValueError:
    pass
else:
    print('ValueError expected')

# Try a format that's too long
try:
    s = _struct.Struct('ii')
except ValueError:
    pass
else:
    print('ValueError expected')

# Try a format with an unknown type
try:
    s = _struct.Struct('z')
except ValueError:
    pass
else:
    print('ValueError expected')

# Try a format with an unknown type
try:
    s = _struct.Struct('P')
except ValueError:
    pass
else:
    print('ValueError expected')

# Try a format with an unknown type
try:
    s = _struct.Struct('c')
except ValueError:
    pass
else:
    print('ValueError expected')

# Try a format with an unknown type
try:
    s = _struct.Struct('b
