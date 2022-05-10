import _struct
# Test _struct.Struct.

# Create a Struct object.
s = _struct.Struct('i')

# Test pack.
print 'pack(i, 1) =', repr(s.pack(1))

# Test pack_into.
buf = bytearray(s.size)
print 'before pack_into:', repr(buf)
s.pack_into(buf, 0, 1)
print 'after pack_into:', repr(buf)

# Test unpack.
print 'unpack(i, "\x01\x00\x00\x00") =', repr(s.unpack('\x01\x00\x00\x00'))

# Test unpack_from.
print 'unpack_from(i, "\x01\x00\x00\x00") =', repr(s.unpack_from('\x01\x00\x00\x00'))

# Test iter_unpack.
print 'iter_unpack(i, "\x01\x00\x00\x00") =', repr(list(s.iter_unpack('
