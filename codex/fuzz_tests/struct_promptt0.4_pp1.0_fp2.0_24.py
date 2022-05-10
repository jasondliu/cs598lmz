import _struct
# Test _struct.Struct.
fmt = 'hhl'
s = _struct.Struct(fmt)
print s.size
print s.pack(1, 2, 3)
print s.pack_into(buffer('xxxxxx'), 3, 1, 2, 3)
print s.unpack('\x01\x00\x02\x00\x03\x00\x04\x00')
print s.unpack_from(buffer('\x01\x00\x02\x00\x03\x00\x04\x00'), 2)
print s.unpack_from(buffer('xxxx\x01\x00\x02\x00\x03\x00\x04\x00'), 4)

# Test _struct.calcsize.
print _struct.calcsize(fmt)

# Test _struct.error.
try:
    _struct.Struct('')
except _struct.error:
    print 'error'

# Test _struct.pack.
print _struct.pack(fmt, 1, 2, 3)
print _struct.pack_
