import _struct
# Test _struct.Struct
print
for t in 'bhil?':
    print '%s:\n%s' % (t, _struct.Struct('999i%s' % t))
print _struct.Struct('5s') == _struct.Struct('5s')
print _struct.Struct('5s') == _struct.Struct('6s')
try:
    _struct.Struct('99999999999d')
except MemoryError as msg:
    print 'MemoryError:', str(msg)
# Test _struct.unpack and _struct.pack.
print
s = _struct.pack('5i', 1, 2, 3, 4, 5)
print 'string: %r' % s, 'as string: %s' % repr(s)
print 'unpack 1:', _struct.unpack('5i', s)
print 'unpack 1, offset 1:', _struct.unpack('4i', s, 1)
print 'unpack 1, offset -1:', _struct.unpack('4i', s, -1)
try:
    print 'unpack 1, offset -201:',
