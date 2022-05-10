import _struct
# Test _struct.Struct

# Test the basic constructors
s = _struct.Struct('i')
s = _struct.Struct('i', _struct.LITTLE_ENDIAN)
s = _struct.Struct('i', _struct.BIG_ENDIAN)
s = _struct.Struct('i', _struct.NETWORK_ORDER)

# Test the various pack/unpack operations
s = _struct.Struct('i')
buf = s.pack(1)
x, = s.unpack(buf)
assert x == 1

s = _struct.Struct('i')
buf = s.pack_into(bytearray(4), 0, 1)
x, = s.unpack_from(buf, 0)
assert x == 1

s = _struct.Struct('i')
buf = bytearray(4)
s.pack_into(buf, 0, 1)
x, = s.unpack_from(buf, 0)
assert x == 1

s = _struct.Struct('i')
buf = bytearray(4)
s.pack_into(memory
