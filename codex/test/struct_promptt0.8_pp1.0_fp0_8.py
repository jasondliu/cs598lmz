import _struct
# Test _struct.Struct.
format = 'hhl'
s = _struct.Struct(format)
print(s.size)
print(s.pack(1, 2, 3))

# Test _struct.pack.
format = 'hhl'
print(_struct.pack(format, 1, 2, 3))

# Test _struct.unpack.
format = 'hhl'
print(_struct.unpack(format, b'\x01\x02\x00\x00\x00\x03\x00\x00\x00'))

# Test _struct.calcsize.
format = 'hhl'
print(_struct.calcsize(format))

# Test _struct.unpack_from.
format = 'hhl'
print(_struct.unpack_from(format, b'\x00\x00\x00\x00\x00\x00\x00\x01\x02\x00\x00\x00\x03\x00\x00\x00', 4))

import _thread

def child(tid):
    print
