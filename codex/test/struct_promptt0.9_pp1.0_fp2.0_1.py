import _struct
# Test _struct.Struct.from_buffer()
assert(_struct.Struct.from_buffer('p', _buffer).format == 'p')
