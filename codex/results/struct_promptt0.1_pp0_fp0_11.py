import _struct
# Test _struct.Struct

# Test that the format string is checked for validity.
try:
    _struct.Struct('Z')
except ValueError:
    pass
else:
    print('ValueError not raised')

# Test that the size is calculated correctly.
s = _struct.Struct('hhl')
if s.size != _struct.calcsize('hhl'):
    print('size error')

# Test that pack returns a bytes object.
s = _struct.Struct('i')
if type(s.pack(1)) is not bytes:
    print('pack error')

# Test that pack_into requires a buffer argument.
try:
    s.pack_into()
except TypeError:
    pass
else:
    print('TypeError not raised')

# Test that pack_into requires a buffer argument.
try:
    s.pack_into(1)
except TypeError:
    pass
else:
    print('TypeError not raised')

# Test that pack_into requires a buffer argument.
try:
    s.pack_into(1, 2, 3, 4)

