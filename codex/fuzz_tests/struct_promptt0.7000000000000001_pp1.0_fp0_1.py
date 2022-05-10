import _struct
# Test _struct.Struct.__new__ with a bad format
try:
    _struct.Struct()
except TypeError:
    pass
else:
    print('failed to raise TypeError with no args')
try:
    _struct.Struct(42)
except TypeError:
    pass
else:
    print('failed to raise TypeError with non-string format')
try:
    _struct.Struct(b'')
except TypeError:
    pass
else:
    print('failed to raise TypeError with empty format')
try:
    _struct.Struct(b'!')
except error:
    pass
else:
    print('failed to raise error with incomplete format')
try:
    _struct.Struct(b'!b')
except error:
    pass
else:
    print('failed to raise error with bad format code')
try:
    _struct.Struct(b'b')
except error:
    pass
else:
    print('failed to raise error with bad format code')
try:
    _struct.Struct(b'!b' * 2 ** 31)
except MemoryError:
    pass
