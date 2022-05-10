import _struct
# Test _struct.Struct.format_size()

s = _struct.Struct('hhl')
print(s.format_size(''))
print(s.format_size('@'))
print(s.format_size('='))
print(s.format_size('<'))
print(s.format_size('>'))
print(s.format_size('!'))

# Test _struct.Struct.size
print(s.size)

# Test _struct.Struct.pack_into()

import array
a = array.array('c', '\0' * s.size)
s.pack_into(a, 0, 1, 2, 3)
print(a)

# Test _struct.Struct.unpack_from()

print(s.unpack_from(a, 0))

# Test _struct.Struct.pack()

print(s.pack(1, 2, 3))

# Test _struct.Struct.unpack()

print(s.unpack(a))

# Test _struct.Struct.iter_unpack()

print(list
