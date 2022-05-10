import _struct
# Test _struct.Struct

# Test _struct.Struct.__new__

# Test _struct.Struct.__new__ with invalid format
try:
    _struct.Struct('x')
except ValueError:
    pass
else:
    print('failed to raise ValueError for invalid format')

# Test _struct.Struct.__new__ with valid format
s = _struct.Struct('i')
if s.format != 'i':
    print('failed to set format correctly')
if s.size != _struct.calcsize('i'):
    print('failed to set size correctly')
if s.format_char != 'i':
    print('failed to set format_char correctly')

# Test _struct.Struct.pack

# Test _struct.Struct.pack with invalid arguments
try:
    s.pack()
except TypeError:
    pass
else:
    print('failed to raise TypeError for missing arguments')

try:
    s.pack(1, 2)
except TypeError:
    pass
else:
    print('failed to raise TypeError for too many arguments')

try:

