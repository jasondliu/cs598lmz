import _struct
# Test _struct.Struct:
s = _struct.Struct('i')
s.size
s.pack(1)
s.unpack(_struct.pack('i', 1))
s.iter_unpack(_struct.pack('ii', 1, 2))
s.iter_unpack(_struct.pack('ii', 1, 2), 2)
# Test _struct.Struct.__new__():
s = _struct.Struct('i', _struct.Struct)
s
s.format
s.size
s.pack(1)
s.unpack(_struct.pack('i', 1))
s.iter_unpack(_struct.pack('ii', 1, 2))
s.iter_unpack(_struct.pack('ii', 1, 2), 2)
# Test _struct.Struct.__new__() with a non-_struct.Struct:
try:
    _struct.Struct('i', int)
except TypeError:
    pass
else:
    print('Failed to raise TypeError')
# Test _struct.Struct.__new__() with a format that differs from the original:
try:
    _struct.
