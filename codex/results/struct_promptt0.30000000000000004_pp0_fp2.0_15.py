import _struct
# Test _struct.Struct

# Test that the format string is checked for validity.
try:
    _struct.Struct('<ii')
except ValueError:
    pass
else:
    print('ValueError not raised')

try:
    _struct.Struct('<iii')
except ValueError:
    pass
else:
    print('ValueError not raised')

try:
    _struct.Struct('<i')
except ValueError:
    pass
else:
    print('ValueError not raised')

# Test that the size is computed correctly.
s = _struct.Struct('<ii')
if s.size != 8:
    print('size', s.size)

# Test that the format string can't be changed.
try:
    s.format = '<iii'
except AttributeError:
    pass
else:
    print('AttributeError not raised')

# Test that the format string can't be deleted.
try:
    del s.format
except AttributeError:
    pass
else:
    print('AttributeError not raised')

# Test pack.
s = _struct.
