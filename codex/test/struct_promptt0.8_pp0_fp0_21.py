import _struct
# Test _struct.Struct.__getstate__
_struct._Struct.__getstate__(Struct('H'))
# Test _struct.Struct.__setstate__
_struct._Struct.__setstate__(Struct('H'), (None, None, None, None, None, None, None, None, None))
_struct._Struct.__setstate__(Struct('H'), ('H', 1, '>', 2, 'H', None, None, None, None))
# Test _struct.Struct.__reduce__
_struct._Struct.__reduce__(Struct('H'))
# Test _struct.Struct.__reduce_ex__
_struct._Struct.__reduce_ex__(Struct('H'))
# Test _struct.Struct.format
_struct._Struct.format(Struct('H'))
# Test _struct.Struct.size
_struct._Struct.size(Struct('H'))

# Test _struct.Struct.unpack
_struct._Struct.unpack(Struct('H'), bytes(2))

