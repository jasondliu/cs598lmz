import _struct
# Test _struct.Struct.__new__

s = _struct.Struct(b'!h')

try:
    _struct.Struct('?h')
except TypeError:
    pass
else:
    print('failed to raise TypeError for invalid code')

try:
    _struct.Struct(b'!')
except _struct.error:
    pass
else:
    print('failed to raise error for bad struct code')

try:
    _struct.Struct('<')
except _struct.error:
    pass
else:
    print('failed to raise error for bad struct code')

try:
    _struct.Struct(b'j')
except _struct.error:
    pass
else:
    print('failed to raise error for bad struct code')

try:
    _struct.Struct(b'@')
except _struct.error:
    pass
else:
    print('failed to raise error for bad struct code')

try:
    _struct.Struct(b'j')
except _struct.error:
    pass
else:
    print('failed to raise error for bad
