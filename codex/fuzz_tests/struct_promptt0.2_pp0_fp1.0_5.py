import _struct
# Test _struct.Struct

# Test the basic methods
s = _struct.Struct('i')
print s.format
print s.size
print s.pack(1)
print s.unpack('\x01\x00\x00\x00')

# Test the pack_into and unpack_from methods
import array
a = array.array('c', '\0' * 8)
s.pack_into(a, 0, 1)
print a
s.pack_into(a, 4, 2)
print a
print s.unpack_from(a, 0)
print s.unpack_from(a, 4)

# Test the __new__ method
s = _struct.Struct('ii')
print s.format
print s.size
print s.pack(1, 2)
print s.unpack('\x01\x00\x00\x00\x02\x00\x00\x00')

# Test the __new__ method with keyword arguments
s = _struct.Struct('ii', byteorder='>')
print s.format
print s.size
print
