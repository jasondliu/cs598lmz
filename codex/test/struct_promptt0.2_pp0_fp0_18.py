import _struct
# Test _struct.Struct

# Test the basic methods

s = _struct.Struct('i')

# Check that the format string is stored
assert s.format == 'i'

# Check that the size is calculated correctly
assert s.size == _struct.calcsize('i')

# Check that the format string can't be changed
try:
    s.format = 'f'
except AttributeError:
    pass
else:
    raise RuntimeError

# Check that the size can't be changed
try:
    s.size = 12
except AttributeError:
    pass
else:
    raise RuntimeError

# Check that we can pack and unpack
assert s.pack(1) == b'\x01\x00\x00\x00'
assert s.unpack(b'\x01\x00\x00\x00') == (1,)

# Check that we can pack_into and unpack_from
buf = bytearray(s.size)
s.pack_into(buf, 0, 1)
