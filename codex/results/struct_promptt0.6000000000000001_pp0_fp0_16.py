import _struct
# Test _struct.Struct
assert isinstance(_struct.Struct('x'), _struct.Struct)
assert isinstance(_struct.Struct('x'), type)
assert _struct.Struct('x').format == 'x'
assert _struct.Struct('x').size == 1
assert _struct.Struct('x').alignment == 1
assert _struct.Struct('x').pack(1) == b'\x01'
assert _struct.Struct('x').unpack(b'\x01') == (1,)
assert _struct.Struct('x').unpack_from(b'\x01', 0) == (1,)

# Test _struct.error
try:
    _struct.Struct('x').pack()
except Exception as e:
    assert isinstance(e, _struct.error)

# Test _struct.pack
assert _struct.pack('x', 1) == b'\x01'
assert _struct.pack('=x', 1) == b'\x01'

# Test _struct.pack_into
buffer = bytearray(1)
_struct.pack_into('x', buffer, 0,
