import _struct
# Test _struct.Struct

# Test _struct.Struct.__new__()

# Test _struct.Struct.__new__() with invalid format
try:
    _struct.Struct('Z')
except ValueError:
    pass
else:
    print('Failed to raise ValueError for invalid format')

# Test _struct.Struct.__new__() with valid format
s = _struct.Struct('i')

# Test _struct.Struct.format
if s.format != 'i':
    print('Failed to set format correctly')

# Test _struct.Struct.size
if s.size != _struct.calcsize('i'):
    print('Failed to set size correctly')

# Test _struct.Struct.pack()

# Test _struct.Struct.pack() with invalid arguments
try:
    s.pack()
except TypeError:
    pass
else:
    print('Failed to raise TypeError for missing arguments')

try:
    s.pack(1, 2)
except TypeError:
    pass
