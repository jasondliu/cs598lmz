from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'i'
s.size = 4
print(s.unpack(b'\x01\x02\x03\x04'))

# Example 3
from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'i'
s.size = 4
print(s.pack(1))

# Example 4
from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'i'
s.size = 4
print(s.pack_into(b'\x00\x00\x00\x00', 0, 1))

# Example 5
from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'i'
s.size = 4
print(s.unpack_from(b'\x01\x02\x03\x04', 0))

# Example 6
from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'i'
s.size = 4
print(s.unpack_from
