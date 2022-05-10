import _struct
# Test _struct.Struct

# Test _struct.Struct.__new__

# Test _struct.Struct.__new__ with invalid format
try:
    _struct.Struct('a')
except ValueError:
    pass
else:
    print('_struct.Struct.__new__ with invalid format failed')

# Test _struct.Struct.__new__ with valid format
try:
    _struct.Struct('i')
except ValueError:
    print('_struct.Struct.__new__ with valid format failed')

# Test _struct.Struct.format

# Test _struct.Struct.format with invalid format
try:
    _struct.Struct('a').format
except ValueError:
    pass
else:
    print('_struct.Struct.format with invalid format failed')

# Test _struct.Struct.format with valid format
try:
    _struct.Struct('i').format
except ValueError:
    print('_struct.Struct.format with valid format failed')

# Test _struct.Struct.size

