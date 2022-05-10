import _struct
# Test _struct.Struct
s = _struct.Struct('hhl')
s.size
# Test _struct.calcsize
s.format
s.pack(1, 2, 3)
a = (1, 2, 3)
s.pack(*a)
s.unpack(s.pack(1, 2, 3))
s.unpack_from(s.pack(1, 2, 3), 0)
s.unpack_from(s.pack(1, 2, 3), 1)
s.unpack_from(s.pack(1, 2, 3), 4)
s.unpack_from(s.pack(1, 2, 3), 5)
s.unpack_from(s.pack(1, 2, 3), 8)
s.unpack_from(s.pack(1, 2, 3), 9)

# Test _struct.Struct.__init__
try:
    _struct.Struct('')
except TypeError:
    print('TypeError')

try:
    _struct.Struct('P')
except TypeError:
    print('TypeError')

