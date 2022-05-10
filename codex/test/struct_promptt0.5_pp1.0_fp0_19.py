import _struct
# Test _struct.Struct
assert _struct.Struct('i') == _struct.Struct('>i')
assert _struct.Struct('<i') == _struct.Struct('i')
assert _struct.Struct('i').size == 4
assert _struct.Struct('i').format == 'i'
assert _struct.Struct('i').pack(123) == b'{'
assert _struct.Struct('i').unpack(b'{') == (123,)
assert _struct.Struct('i').unpack_from(b'{') == (123,)
assert _struct.Struct('i').unpack_from(b'{', 0) == (123,)
assert _struct.Struct('i').unpack_from(b'{', 1) == ()
assert _struct.Struct('i').unpack_from(b'', 0) == ()
assert _struct.Struct('i').unpack_from(b'', 1) == ()

assert _struct.Struct('i').pack_into(bytearray(10), 0, 123) == None
