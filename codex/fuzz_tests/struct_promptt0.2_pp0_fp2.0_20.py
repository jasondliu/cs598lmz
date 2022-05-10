import _struct
# Test _struct.Struct

# Test _struct.Struct.__new__

# Test _struct.Struct.__new__ with invalid format
try:
    _struct.Struct('z')
except ValueError:
    pass
else:
    print('Failed to raise ValueError for invalid format')

# Test _struct.Struct.__new__ with valid format
s = _struct.Struct('i')

# Test _struct.Struct.format
if s.format != 'i':
    print('Failed to set format correctly')

# Test _struct.Struct.size
if s.size != _struct.calcsize('i'):
    print('Failed to set size correctly')

# Test _struct.Struct.pack
if s.pack(1) != _struct.pack('i', 1):
    print('Failed to pack correctly')

# Test _struct.Struct.unpack
if s.unpack(s.pack(1)) != (1,):
    print('Failed to unpack correctly')

# Test _struct.Struct.iter_unpack
if list(s.iter_un
