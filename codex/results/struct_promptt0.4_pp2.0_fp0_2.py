import _struct
# Test _struct.Struct

# Test the basic methods

s = _struct.Struct('i')

print s.format
print s.size
print s.pack(1)
print s.unpack(s.pack(1))

# Test the __new__ method

s = _struct.Struct('i', True)

print s.format
print s.size
print s.pack(1)
print s.unpack(s.pack(1))

# Test the __repr__ method

print repr(s)

# Test the __str__ method

print str(s)

# Test the pack_into method

a = array('c', '123456789')
s.pack_into(a, 1, 1)
print a

# Test the unpack_from method

print s.unpack_from(a, 1)

# Test the iter_unpack method

print list(s.iter_unpack(a))

# Test the pack method with too many arguments

try:
    print s.pack(1, 2)
except TypeError:

