import _struct
# Test _struct.Struct.
fmt = 'hhl'
s = _struct.Struct(fmt)
buf = s.pack(1, 2, 3)
print(s.unpack(buf))
print(s.unpack_from(buf))
print(s.calcsize())

fmt = 'hhl'
s = _struct.Struct(fmt)
buf = s.pack(1, 2, 3)
print(s.unpack(buf))
print(s.unpack_from(buf))
print(s.calcsize())

# Test _struct.error.
try:
    s = _struct.Struct('z')
except _struct.error as e:
    print(e)
else:
    raise RuntimeError('expected _struct.error')

# Test _struct.pack.
print(_struct.pack('hhl', 1, 2, 3))

# Test _struct.pack_into.
buf = bytearray(12)
_struct.pack_into('hhl', buf, 0, 1, 2, 3)
print(buf)

#
