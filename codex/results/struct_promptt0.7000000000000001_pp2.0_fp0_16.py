import _struct
# Test _struct.Struct
struct = _struct.Struct('c')
assert struct.size == 1
assert struct.pack(b'x') == b'x'
assert struct.unpack(b'x') == (b'x',)
assert struct.pack_into(b'x', b'a') == b'a'
assert struct.pack_into(b'x', b'a', 0) == b'a'
assert struct.unpack_from(b'x', b'a') == (b'x',)
assert struct.unpack_from(b'x', b'a', 0) == (b'x',)
assert struct.format == 'c'

# Test _struct.Struct.__new__
assert _struct.Struct('c') is _struct.Struct('c')
assert _struct.Struct('c') is not _struct.Struct('b')

# Test _struct.Struct.__call__
struct = _struct.Struct('c')
assert struct(b'x') == b'x'

# Test _struct.Struct.__eq__
assert _struct.Struct('c')
