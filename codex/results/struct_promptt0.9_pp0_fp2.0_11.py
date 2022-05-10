import _struct
# Test _struct.Struct
h = _struct.Struct('hhl')
print h
print 'Size of _struct.Struct: ', h.size
print
t = h.pack(2,4,1)
print h.unpack(t)
print
t = h.pack(0,3,3)
print h.unpack(t)
print
t = h.pack(1,2,0)
print h.unpack(t)

print
print 75 * "-"

# Test struct as Simple Namespace
import struct as s
print s
print 'Size of struct as Simple Namespace : ', s.calcsize('hhl')
print
t = s.pack('hhl', 2,4,1)
print s.unpack('hhl', t)
print
t = s.pack('hhl', 0,3,3)
print s.unpack('hhl', t)
print
t = s.pack('hhl', 1,2,0)
print s.unpack('hhl', t)

print
print 75 * "-"

# Test struct methods
import _struct
