import _struct
# Test _struct.Struct.pack_into

s = _struct.Struct('i')

# First without buffer
with pytest.raises(_struct.error) as excinfo:
    s.pack_into('ii', [2,3])
assert str(excinfo.value) == 'buffer is too small for data'

# Then with buffer
b = bytearray(4)
s.pack_into('ii', b, 2, 2, 3)
assert b == b'\x00\x00\x02\x00\x00\x00\x03'

# Test the remainder of _struct.Struct.pack_into errors
with pytest.raises(_struct.error) as excinfo:
    s.pack_into('ii', b'12345', 2, 2, 3)
assert str(excinfo.value) == 'buffer is too small for data'

