import _struct
# Test _struct.Struct

# Test that the format string is handled correctly
s = _struct.Struct('hhl')
print s.size
print s.format

# Test that packing works
x = s.pack(1, 2, 3)
print x
print len(x)

# Test unpacking
print s.unpack(x)

# Test endian-ness
s = _struct.Struct('>hhl')
print s.size
print s.format

# Test that packing works
x = s.pack(1, 2, 3)
print x
print len(x)

# Test unpacking
print s.unpack(x)

# Test that we can use buffer objects
b = buffer(x)
print s.unpack(b)

# Test that we can use array objects
import array
a = array.array('b', x)
print s.unpack(a)

# Test that we can use memoryview objects
m = memoryview(x)
print s.unpack(m)

# Test that we can use buffer objects
b = buffer(x)
print
